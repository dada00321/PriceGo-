# PriceGo-
Compare merchandises for a given searching keyword, also can add to favorite-list. Underpinned by crawling some shopping website.

目前有的功能:
1. 輸入搜尋商品
2. 爬蟲購物網站資訊
3. 顯示結果在 GUI 上
4. 對不同欄位排序
5. 按下追蹤按鈕，將加入至資料庫
(使用 PHPViewer, HeidiSQL9)
6. 查看及排序追蹤清單

未來想加的功能: 
1. 追蹤清單和爬蟲結果，可以做刪除該筆商品的功能
2. 將爬蟲結果儲存為excel檔案。當搜尋先前已搜尋過的商品時，可選擇是否以excel檔載入(或重新爬蟲)
3. 使用多執行緒，提高運行效率
4. 商品推薦功能: 以用戶儲存的追蹤清單為推薦的依據
5. 使用NLP中文分詞技術，將每筆搜尋結果的商品名稱分為不同標籤，提高商品搜尋的精準度。
(如: 搜尋: "島風"，會出現 "巴里島風編織扇..."。若能利用分詞模組拆解商品名稱，就可以過濾不相關的結果)
