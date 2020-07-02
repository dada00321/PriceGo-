import time
import json
from modules.basic_scraping_module import get_response, get_soup, download_pic
from modules.file_process_module import save_API_n_results_to_txt

class Shopee_Crawler():
    def __init__(self, merchandise_name):
        if merchandise_name != "":
            self.merchandise_name = merchandise_name
        else: print("輸入不可為空")
    
    def get_page_amount(self):
        easy_searchUrl = f"https://shopee.tw/search?keyword={self.merchandise_name}"
        
        r = get_response(easy_searchUrl)
        if r != None:
            soup = get_soup(r)
            div_not_found = soup.find(text="我們找不到")
            div_not_found_2 = soup.find(text="未找到商品")
            if (div_not_found != None) or (div_not_found_2 != None):
                print(f"未找到商品 \'{self.merchandise_name}\'")
            
            self.page_amount = int(soup.find("span", class_="shopee-mini-page-controller__total").text) 
            print(f"已找到商品 \'{self.merchandise_name}\'")
            print(f"共找到 {self.page_amount} 頁")
            print("=========================")
        else:
            self.page_amount = -1
            print("[get_page_amount] Cann't get response.")
            print("status code:", r.status_code)
        
    def generate_firstAPI_URLs(self):
        searchPage_url = ["https://shopee.tw/api/v2/search_items/?by=relevancy",
                          f"&keyword={self.merchandise_name}",
                          "&limit=50&newest={}", #pageNum*50
                          "&order=desc&page_type=search&version=2"]
        URLs = []
        for pageNum in range(self.page_amount):
            url = ''.join(searchPage_url[0:2]) + searchPage_url[2].format(pageNum*50) + searchPage_url[-1]
            URLs.append(url)
        return URLs
    
    def visit_firstAPI_URLs(self, firstAPI_URLs):
        count_No = 1
        self.firstAPI_results = []
        print("正在對 firstAPI 進行爬蟲")
        ''' 拜訪 "所有"商品查詢結果頁的API網址 '''
        for page_n, searchPage_url in enumerate(firstAPI_URLs):
            print(f"正在爬 第 {page_n+1} 頁...")
            print(f"API-1網址:\n  {searchPage_url}")
            if page_n > 1: break    # only test the first page
            #print(f"count_No: {count_No}")
            r = get_response(searchPage_url)
            if r != None:
                API_searchPage_data = json.loads(r.text)
                ''' 對API獲取的 "單頁" 商品資訊爬蟲 '''
                for item_idx in range(50): #單頁上限50筆資料
                    try:
                        itemid = API_searchPage_data["items"][item_idx]["itemid"]
                        shopid = API_searchPage_data["items"][item_idx]["shopid"]
                        '''
                        判斷 itemid, shopid 是否重複出現在 firstAPI_results
                        '''
                        currLength = len(self.firstAPI_results)
                        recorded_itemids = [self.firstAPI_results[_]["itemid"] for _ in range(currLength)]
                        recorded_shopids = [self.firstAPI_results[_]["shopid"] for _ in range(currLength)]
                        if (itemid in recorded_itemids) or (shopid in recorded_shopids):
                            print("該商品重複出現，故不記錄")
                            continue
                        # 若是不曾記錄過的商品則加入 firstAPI_results
                        self.firstAPI_results.append({"No":count_No,"itemid":itemid,"shopid":shopid})
                        count_No += 1
                    except IndexError: # list index out of range
                        ''' 因為最後一頁未必有50筆資料，故會發生IndexError
                            當捕捉到此例外，就跳出迴圈'''
                        print("已達最後一筆，商品資訊抓取完畢")
                        break  
                print(f"第 {page_n+1} 頁爬蟲完畢！\n")
            else:
                print(f"Fail to get response.(Page: {page_n+1})")
        print("API-1 所有頁面皆爬蟲完畢！", "="*25, sep='')
        
    def go_unique(self, itemid, shopid, No):
        ''' 特定商品頁API: 爬價格 & 圖片 & 其它欄位 '''
        #itemid = "1447308880"; shopid = "2971543" #斧乃木
        #itemid=4623462091; shopid=4278725 # 口罩
        #itemid=5811180671; shopid=37065645 # 手機殼 小米
        
        mdsePage_url = f"https://shopee.tw/api/v2/item/get?itemid={itemid}&shopid={shopid}"
        r = get_response(mdsePage_url)
        if r != None:
            API_mdsePage_data = json.loads(r.text)
            item = API_mdsePage_data["item"]
            '''
            if item["models"] == []: # 單一規格
                print("rrrr")
            else:  # 多種規格
                print("www") # <-- 需針對不同規格的價錢, 種類名稱等細分 (models)
            '''
            # 商品名稱:
            fullname = item["name"]
            # 商品價格:(初始顯示金額)
            price_max = int(str(item["price_max"])[:-5])
            price_min = int(str(item["price_min"])[:-5])
            price_avg = price_max
            if  price_max != price_min: 
                price_avg = (price_max + price_min) // 2
                
            # 商品參考圖片:
            ''' images = item["images"] # type: list '''
            image = item["images"][0] # <-- 一串亂碼, 但加上其他部份後可對應到圖片網址
            #image_path = f".\{self.merchandise_name}_商品圖片\{No}.jfif"
            #print(f"第 {No} 項商品圖片正在下載中")
            download_pic(self.merchandise_name, image, No) # 下載單一商品圖片
            
            # 商品規格:
            brand = item["brand"] # 1.品牌
            stock = item["stock"] # 2.庫存
            location = item["shop_location"] # 3.出貨地
            # "喜歡"次數:
            liked_count = item["liked_count"]
            # 已售出數量:
            historical_sold = item["historical_sold"]
            # 商品詳情:
            description = item["description"] 
            
            secondAPI_result = {"name": fullname,
                                "price_max": price_max,
                                "price_min": price_min,
                                "price_avg": price_avg,
                                "historical_sold": historical_sold,
                                "stock": stock,
                                "location": location,
                                "liked_count": liked_count,
                                "brand": brand,
                                "image": image,
                                "description": description,
                                }
            # replace None with empty string in sake of storing to DB correctly in GUI  
            for key, value in secondAPI_result.items():
                if value == None:
                    secondAPI_result[key] = '' 
            #print(secondAPI_result)
            return secondAPI_result
        else:
            print(f"Fail to obtain the information of item {No} from API-2")
            return None
        
    def get_firstAPI_results(self):
        return self.firstAPI_results
        
    def get_mdse_infos(self):
        return self.mdse_infos
    
    def shopee_crawling_firstAPI(self):
        t0 = time.time()
        self.get_page_amount() # 取得查詢商品總頁數
        
        if self.page_amount != -1:
            firstAPI_URLs = self.generate_firstAPI_URLs()
            self.visit_firstAPI_URLs(firstAPI_URLs)
            
            if len(self.firstAPI_results) > 0:
                # (optional) 將 No, itemid, shopid 3 欄位 為一筆 list 元素組成的有用資訊 (type: list) 以 txt保存
                save_API_n_results_to_txt(self.merchandise_name, self.firstAPI_results, 1)
                firstAPI_exeTime = time.time()-t0
                print(f"API-1 => Execution time: {firstAPI_exeTime} sec")
                return firstAPI_exeTime

if __name__ == "__main__":
    mdse_name = "酒精"
    crawler = Shopee_Crawler(mdse_name)
    '''
    crawler.shopee_crawling()
    #print(crawler.mdse_infos)
    mdse_infos = crawler.get_mdse_infos()
    print("mdse_infos:", mdse_infos)
    '''
