import requests as rs
from bs4 import BeautifulSoup as bs
import os

def get_response(url):
    headers = {"User-Agent": "Googlebot",}
    r = rs.get(url, headers=headers)
    if r.status_code == rs.codes.ok: 
        r.encoding = "utf-8"
        return r
    else:
        print("Fail to get response.")
        return None
    
def get_soup(response):
    return bs(response.text, "lxml")

def download_pic(merchandise_name, image, No):
    pic_url = f"https://cf.shopee.tw/file/{image}_tn"
    r = get_response(pic_url)
    if r != None:        
        mdsePics_dir = f"{merchandise_name}_商品圖片"
        if not os.path.exists(mdsePics_dir):
            os.mkdir(mdsePics_dir)
        try:
            mdsePic_path = f"{mdsePics_dir}/{No}.jfif"
            with open(mdsePic_path, "wb") as fp:
                fp.write(r.content)
            print(f"第 {No} 件商品獲取圖片成功！")
        except:
            print(f"第 {No} 件商品獲取圖片失敗 (Fail to store image into the merchandise's directory)")
    else:
        print(f"第 {No} 件商品獲取圖片失敗 (Fail to get request)")