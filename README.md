# PriceGo-
Compare merchandises for a given searching keyword, also can add to favorite-list. Underpinned by crawling some shopping website.

I. 使用限制:

  1.
    因本程式儲存追蹤商品的資料庫部分僅以本機伺服器、DBMS做一個簡易的應用。故使用前需先下載 HeidiSQL9 及 PHPViewer，方能使用 "加入追蹤商品" 功能。
    (可至"附件下載"的雲端鏈結中下載，包含這兩個檔案的壓縮檔)

  2.
  (1)Shopee_Crawler_v1_2.py 
    ∟ Line 51: if page_n > 1: break    # only test the first page
    --> 可自行在前方加上#註解，以爬取搜尋結果的所有頁面
  
  (2)layout_v2_9.py
    ∟ Line 438: #if No==6: break  # only test the top 5 data
    --> 同上

II. 附件下載: (共用的Google雲端鏈結)
https://drive.google.com/drive/folders/149JYwkfiHdnY_CJuejtEtkINx4D15Dah

III. Demo影片:
https://www.youtube.com/watch?v=0-ttEgsAhns

IV. 目前有的功能:
1. 輸入搜尋商品
2. 爬蟲購物網站資訊
3. 顯示結果在 GUI 上
4. 對不同欄位排序
5. 按下追蹤按鈕，將加入至資料庫
(使用 PHPViewer, HeidiSQL9)
6. 查看及排序追蹤清單

V. 未來想加的功能: 
1. 增加一個欄位，點選後可開啟超鏈結，顯示該商品的實際網頁
2. 追蹤清單和爬蟲結果，可以做刪除該筆商品的功能
3. 將爬蟲結果儲存為excel檔案。當搜尋先前已搜尋過的商品時，可選擇是否以excel檔載入(或重新爬蟲)
4. 使用多執行緒，提高運行效率
5. 商品推薦功能: 以用戶儲存的追蹤清單為推薦的依據
6. 使用NLP中文分詞技術，將每筆搜尋結果的商品名稱分為不同標籤，提高商品搜尋的精準度。
(如: 搜尋: "島風"，會出現 "巴里島風編織扇..."。若能利用分詞模組拆解商品名稱，就可以過濾不相關的結果)
