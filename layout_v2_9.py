# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Shopee_Crawler_v1_2 import Shopee_Crawler
from modules.file_process_module import move_mdseInfo_to_dest, save_API_n_results_to_txt
from modules.DB_assistant import save2db, view_db
import string
import time
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        MainWindow.setObjectName("MainWindow")
        GUI_width = 1530; GUI_height = 910
        MainWindow.resize(GUI_width, GUI_height)
        MainWindow.setCentralWidget(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Agency FB") # font type
        font.setPointSize(18)
        
        self.dataSrc = None
        
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(650, 10, 120, 100))
        self.btnQuery.setFont(font)
        self.btnQuery.setObjectName("btnQuery")
        
        self.default_icon = QtGui.QIcon(QtGui.QPixmap(r".\res\icon\addBtn3.png"))
        self.default_icon_size = QtCore.QSize(130, 200)
        
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(30, 20, 241, 51))
        self.lbl_1.setFont(font)
        self.lbl_1.setObjectName("lbl_1")
        
        self.edtMdse = QtWidgets.QLineEdit(self.centralwidget)
        self.edtMdse.setGeometry(QtCore.QRect(270, 20, 341, 51))
        self.edtMdse.setFont(font)
        self.edtMdse.setObjectName("edtMdse")
        
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(30, 80, 141, 41))
        self.lbl_2.setFont(font)
        self.lbl_2.setObjectName("lbl_2")
        
        self.tableMdse = QtWidgets.QTableWidget(self.centralwidget)
        self.tableMdse.setGeometry(QtCore.QRect(50, 140, 1430, 700))
        self.tableMdse.setObjectName("tableMdse")
        self.tableMdse.setColumnCount(11)
        self.tableMdse.setRowCount(0)
        # 設定水平表頭, 隱藏垂直表頭:
        self.tableMdse.setHorizontalHeaderLabels(["編號","加入追蹤","商品名稱","價格(NTD)","銷量","庫存","出貨地","喜歡次數","品牌","商品參考圖片","詳細資訊"])  
        self.tableMdse.verticalHeader().setVisible(False)
        
        self.mdseImg_size = 200
        self.tableMdse.setIconSize(QtCore.QSize(self.mdseImg_size, self.mdseImg_size))
        col_sizes = [70,130,190,90,90,90,140,90,140,200,200]
        for i in range(len(col_sizes)):
           self.tableMdse.setColumnWidth(i , col_sizes[i])
        self.tableMdse.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # 將表格變成禁止編輯
        #self.tableMdse.resizeColumnsToContents()
        self.tableMdse.resizeRowsToContents()
        
        self.conLayout = QtWidgets.QHBoxLayout()
        self.conLayout.addWidget(self.tableMdse)
        self.setLayout(self.conLayout)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, GUI_width, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.mdse_search = QtWidgets.QAction(MainWindow)
        self.mdse_search.setObjectName("mdse_search")
        self.sort_by_price_ASC = QtWidgets.QAction(MainWindow)
        self.sort_by_price_ASC.setObjectName("sort_by_price_ASC")
        self.sort_by_price_DESC = QtWidgets.QAction(MainWindow)
        self.sort_by_price_DESC.setObjectName("sort_by_price_DESC")
        self.sort_by_soldNum_DESC = QtWidgets.QAction(MainWindow)
        self.sort_by_soldNum_DESC.setObjectName("sort_by_soldNum_DESC")
        self.sort_by_soldNum_ASC = QtWidgets.QAction(MainWindow)
        self.sort_by_soldNum_ASC.setObjectName("sort_by_soldNum_ASC")
        self.sort_by_stock_DESC = QtWidgets.QAction(MainWindow)
        self.sort_by_stock_DESC.setObjectName("sort_by_stock_DESC")
        self.sort_by_stock_ASC = QtWidgets.QAction(MainWindow)
        self.sort_by_stock_ASC.setObjectName("sort_by_stock_ASC")
        self.sort_by_liked_count_DESC = QtWidgets.QAction(MainWindow)
        self.sort_by_liked_count_DESC.setObjectName("sort_by_liked_count_DESC")
        self.sort_by_liked_count_ASC = QtWidgets.QAction(MainWindow)
        self.sort_by_liked_count_ASC.setObjectName("sort_by_liked_count_ASC")
        self.view_favorites = QtWidgets.QAction(MainWindow)
        self.view_favorites.setObjectName("view_favorites")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.mdse_search)
        self.menu_2.addAction(self.sort_by_price_DESC)
        self.menu_2.addAction(self.sort_by_price_ASC)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.sort_by_soldNum_DESC)
        self.menu_2.addAction(self.sort_by_soldNum_ASC)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.sort_by_stock_DESC)
        self.menu_2.addAction(self.sort_by_stock_ASC)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.sort_by_liked_count_DESC)
        self.menu_2.addAction(self.sort_by_liked_count_ASC)
        self.menu_2.addSeparator()
        self.menu_3.addAction(self.view_favorites)
        self.menu_4.addAction(self.exit)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.setting_funcs(MainWindow)
        
        #self.menu_1_widgets = [self.btnQuery,self.lbl_1,self.lbl_2,self.edtMdse,self.tableMdse]
        #self.menu_2_selected(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def reset_search(self):
        if self.dataSrc != None:
            self.dataSrc = None
            self.mdse_infos = []
            self.favorites = []
            self.tableMdse.setRowCount(0)
            QtWidgets.QApplication.processEvents() # 刷新頁面
    
    def menu_1_selected(self, q): ###
        #self.tableMdse.setHidden(True)
        #[widget.setHidden(False) for widget in self.menu_1_widgets]
        self.statusBar().showMessage(f"{q.text()} is triggered", 3000)
    
    def update_unique_for_favoriates(self, item, idx):
        imgPath = f"{self.imgsPath}\{item[0]}.jfif"
        
        # No(商品編號): 依爬蟲順序(網頁元素擺放順序) 從 1 累加
        newItem = QtWidgets.QTableWidgetItem(str(item[0]))
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 0, newItem)
        # '加入追蹤' 按鈕
        btnAdd = QtWidgets.QPushButton()
        btnAdd.setIcon(self.default_icon)
        btnAdd.setIconSize(self.default_icon_size)
        #btnAdd.setDown(True)
        btnAdd.setStyleSheet("QPushButton{margin:3px};")
        btnAdd.clicked.connect(self.btnAdd_clicked)
        self.tableMdse.setCellWidget(idx, 1, btnAdd)
        # 商品名稱
        newItem = QtWidgets.QTableWidgetItem(item[3]) 
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 2, newItem)
        # 價格
        price_max = item[4]
        price_min = item[5]
        price_avg = item[6]
        #show_price = f"NTD ${price_max}"
        show_price = f"${price_max}"
        if price_max != price_min:
            show_price = f"平均價格: ${price_avg}\n"
            show_price += f"${price_min}\n ~ \n${price_max}"
        newItem = QtWidgets.QTableWidgetItem(show_price)
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 3, newItem)
        # 已售出數量
        newItem = QtWidgets.QTableWidgetItem(str(item[7]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 4, newItem)
        # 庫存
        newItem = QtWidgets.QTableWidgetItem(str(item[8]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 5, newItem)
        # 出貨地
        newItem = QtWidgets.QTableWidgetItem(item[9])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 6, newItem)
        # 喜歡次數
        newItem = QtWidgets.QTableWidgetItem(str(item[10]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 7, newItem)
        # 品牌
        newItem = QtWidgets.QTableWidgetItem(item[11])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 8, newItem)
        # 商品參考圖片 // 抓第一張(預覽圖)就好
        newItem = QtWidgets.QTableWidgetItem(QtGui.QIcon(imgPath), "")
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 9, newItem)
        # 商品詳情
        newItem = QtWidgets.QTableWidgetItem(item[13])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 10, newItem)
        
    def update_unique(self, item, idx, srcType):
        if srcType == 1:     # btnQuery_clicked
            imgPath = f".\{self.merchandise_name}_商品圖片\{item['No']}.jfif"
        elif srcType == 2:   # sort_by_XXX selected
            imgPath = f"{self.imgsPath}\{item['No']}.jfif"

        # No(商品編號): 依爬蟲順序(網頁元素擺放順序) 從 1 累加
        newItem = QtWidgets.QTableWidgetItem(str(item["No"]))
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 0, newItem)
        
        # '加入追蹤' 按鈕
        btnAdd = QtWidgets.QPushButton()
        btnAdd.setIcon(self.default_icon)
        btnAdd.setIconSize(self.default_icon_size)
        #btnAdd.setDown(True)
        btnAdd.setStyleSheet("QPushButton{margin:3px};")
        btnAdd.clicked.connect(self.btnAdd_clicked)
        self.tableMdse.setCellWidget(idx, 1, btnAdd)
        
        # 商品名稱
        newItem = QtWidgets.QTableWidgetItem(item["name"]) 
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 2, newItem)
        # 價格
        price_max = item["price_max"]
        price_min = item["price_min"]
        price_avg = item["price_avg"]
        #show_price = f"NTD ${price_max}"
        show_price = f"${price_max}"
        if item["price_max"] != item["price_min"]:
            show_price = f"平均價格: ${price_avg}\n"
            show_price += f"${price_min}\n ~ \n${price_max}"
        newItem = QtWidgets.QTableWidgetItem(show_price)
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter) 
        self.tableMdse.setItem(idx, 3, newItem)
        
        # 已售出數量
        newItem = QtWidgets.QTableWidgetItem(str(item["historical_sold"]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 4, newItem)
        # 庫存
        newItem = QtWidgets.QTableWidgetItem(str(item["stock"]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 5, newItem)
        # 出貨地
        newItem = QtWidgets.QTableWidgetItem(item["location"])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 6, newItem)
        # 喜歡次數
        newItem = QtWidgets.QTableWidgetItem(str(item["liked_count"]))  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 7, newItem)
        # 品牌
        newItem = QtWidgets.QTableWidgetItem(item["brand"])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 8, newItem)
        # 商品參考圖片 // 抓第一張(預覽圖)就好
        newItem = QtWidgets.QTableWidgetItem(QtGui.QIcon(imgPath), "")
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 9, newItem)
        # 商品詳情
        newItem = QtWidgets.QTableWidgetItem(item["description"])  
        newItem.setTextAlignment(QtCore.Qt.AlignHCenter| QtCore.Qt.AlignVCenter)
        self.tableMdse.setItem(idx, 10, newItem)
        
    def update_table(self):
        if self.dataSrc == "mdse_infos":
            for idx, record in enumerate(self.mdse_infos):
                self.update_unique(record, idx, 2)
        elif self.dataSrc == "favorites":
            self.tableMdse.setRowCount(0)
            QtWidgets.QApplication.processEvents() # 刷新頁面
            #-------------------------------------------------
            self.tableMdse.setRowCount(len(self.favorites))
            for idx, record in enumerate(self.favorites):
                self.tableMdse.setRowHeight(idx, self.mdseImg_size)
                self.update_unique_for_favoriates(record, idx)
        
    def update_table_withFavorites(self):
        if self.dataSrc == "mdse_infos":
            # 顯示提示訊息
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle("重複確認")
            box.setText("確定要查看追蹤商品嗎？\n先前的搜尋記錄會遺失喔")
            box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText("確定")
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText("取消")
            box.exec_()
            if box.clickedButton() == buttonY: # 'YES' pressed
                self.dataSrc = "favorites"
                #print("\n正在讀取追蹤清單，請稍等...")
                self.statusBar().showMessage("正在讀取追蹤清單，請稍等...")
                self.favorites = view_db(self.merchandise_name)
                self.update_table()
                #print("追蹤清單載入成功\n")
                self.statusBar().showMessage("追蹤清單載入成功")
        elif self.dataSrc == None:
            #print("尚未進行搜尋，搜尋後方可查看追蹤商品\n")
            self.statusBar().showMessage("尚未進行搜尋，搜尋後方可查看追蹤商品")
        
    def get_clean_fields(self, row):
        record = self.mdse_infos[row]
        # 3(API-1) + 11(API-2) 共 14 個欄位
        ''' Check & clean possible errors for all fields in the selected row '''
        err_types = []
        #------------------------------
        # type-1 error: 'API-1 results' OUT OF RANGE
        block_1 = [record["No"], record["itemid"], record["shopid"]]
        if len(str(block_1[0])) > 10 or len(str(block_1[1])) > 11 or len(str(block_1[2])) > 10: 
            err_types.append(1)
        #------------------------------
        # type-2 error: used bits of 'image'(API-2) reference OUT OF RANGE
        block_2 = [record["image"]]
        if len(block_2[0]) > 32:
            err_types.append(2)
        #------------------------------
        # type-3 error: total bits of 'prices'(API-2) OUT OF RANGE (greater than 8 bits)
        block_3 = [record["price_max"], record["price_min"], record["price_avg"]]
        invalid_count = len([p for p in (block_3[0],block_3[1],block_3[2]) if (len(str(p)) > 8)])
        if invalid_count != 0:
            err_types.append(3)
        #------------------------------
        # type-4 error: 'numeric-fields'(API-2) OUT OF RANGE
        block_4 = [record["historical_sold"], record["stock"], record["liked_count"]]
        if len(str(block_4[0]))>8 or len(str(block_4[1]))>8 or len(str(block_4[2]))>6: 
            err_types.append(4)
        #------------------------------
        # type-5 error: 'NVARCHAR'(API-2) out of range -> still can work!
        block_5 = [record["name"], record["location"], record["brand"], record["description"]]
        
        pattern = "[^a-zA-Z0-9\u4e00-\u9fa5 ]"
        for i in ([0, -1]):
            block_5[i] = block_5[i].replace("\n", "")
            block_5[i] = re.sub(pattern, "", block_5[i])
        s = ""
        for word in block_5[-1].split():
            s += word.strip(string.punctuation)
        block_5[-1] = s
        
        cropping = lambda field, upperbounds, idx: field[:(upperbounds[idx]-3)] + "..."
        upperbounds = [60, 20, 20, 250]
        for idx in range(len(block_5)):
            if len(block_5[idx]) > upperbounds[idx]:
                if 5 not in err_types:    err_types.append(5)
                block_5[idx] = cropping(block_5[idx], upperbounds, idx)
        
        ''' Print testing message '''
        """
        msg = "※ 商品資訊摘要\n"
        msg += f"No: {block_1[0]}\n";
        msg += f"name: {block_5[0]}\n"
        msg += f"price: {block_3[1]} ~ {block_3[0]}\n\n"
        print(msg)
        """
        print(f"檢查資料格式...")
        if len(err_types) == 0:
            #print("全部欄位皆符合 DB schema\n")
            self.statusBar().showMessage("全部欄位皆符合 DB schema")
            return (block_1, block_2, block_3, block_4, block_5)
        elif len(err_types)==1 and 5 in err_types:
            #print("已修正過長的文字欄位")
            self.statusBar().showMessage("已修正過長的文字欄位")
            return (block_1, block_2, block_3, block_4, block_5)
        else:
            print("資料格式有誤！無法順利加入資料庫")
            print(f"共 {len(err_types)} 個欄位不符合 DB schema")
            print("error types: ", *(e for e in err_types))
            return None
    
    def save_to_DB(self, row):
        fields = self.get_clean_fields(row)
        if fields != None:
            values = f"{fields[0][0]}, {fields[0][1]}, {fields[0][2]}, "
            values += f"\'{fields[4][0]}\', "
            values += f"{fields[2][0]}, {fields[2][1]}, {fields[2][2]}, "
            values += f"{fields[3][0]}, {fields[3][1]}, \'{fields[4][1]}\', "
            values += f"{fields[3][2]}, \'{fields[4][2]}\', "
            values += f"\'{fields[1][0]}\', \'{fields[4][3]}\'"
            #print("INSERT VALUES:", values)
            save2db(self.merchandise_name, values)
    
    def btnAdd_clicked(self):
        button = self.sender()
        index = self.tableMdse.indexAt(button.pos())
        if index.isValid():
            row_ = index.row()
            self.statusBar().showMessage(f"正在將 No: {self.mdse_infos[row_]['No']} 的商品加入資料庫")
            #print(f"正在將 No: {self.mdse_infos[row_]['No']} 的商品加入資料庫")
            self.save_to_DB(row_)
            
    def btnQuery_clicked(self):
        self.dataSrc = "mdse_infos"
        self.merchandise_name = self.edtMdse.text()
        if self.merchandise_name != "":
            '''
            Get the merchandise info list
            '''
            print(f"　開始搜尋 {self.merchandise_name} ...")
            crawler = Shopee_Crawler(self.merchandise_name)
            
            # 逐一更新商品:
            # 1.先取得所有 API-1 結果 (並回傳 API-1 運行時間)
            firstAPI_exeTime = crawler.shopee_crawling_firstAPI()
            #print(f"　{self.merchandise_name} API-1資訊皆取完畢")
            self.statusBar().showMessage(f"　{self.merchandise_name} API-1資訊皆取完畢")
            firstAPI_results = crawler.get_firstAPI_results()
            
            t1 = time.time() # 開始計時 API-2
            n_mdse = 0 # API-2 成功爬取的商品數量, 由 0 遞增
            self.mdse_infos = []
            # 2.取得成功爬取的所有API-2結果, 並放入 'self.mdse_infos' 長期保存 (供排序等模組使用)
            for idx, item in enumerate(firstAPI_results):
                # 每個 item 是一個字典, 有 3 keys: "No", "itemid", "shopid"
                No, itemid, shopid = item.values()
                
                #if No==6: break  # only test the top 3 data
                
                #print(f"　開始爬 第 {No} 件商品")
                self.statusBar().showMessage(f"　開始爬 第 {No} 件商品")
                # 11 keys: "name" ~ "description"
                curr_mdse_dict = {"No":No, "itemid":itemid, "shopid":shopid}
                secondAPI_result = crawler.go_unique(itemid, shopid, No)
                for key, value in secondAPI_result.items():
                    curr_mdse_dict[key] = value
                #print("secondAPI_result:", secondAPI_result)
                if secondAPI_result != None:
                    n_mdse += 1
                    ''' 若成功取得API-2 results(type: dict)，則連同 API-1 results，
                    組合成新的 dictionary，加入 self.mdse_infos 串列 '''
                    #self.mdse_infos.append(secondAPI_result)
                    self.mdse_infos.append(curr_mdse_dict)
                    #print(f"　第 {No} 件商品資訊爬蟲成功！\n")
                    self.statusBar().showMessage(f"　第 {No} 件商品資訊爬蟲成功！")
                    # Update table
                    self.tableMdse.setRowCount(n_mdse)
                    self.tableMdse.setRowHeight(n_mdse-1, self.mdseImg_size)
                    self.update_unique(curr_mdse_dict, n_mdse-1, 1)
                    # 刷新頁面(少了這行會lag, 且所有資料都獲取完畢才會刷新介面):
                    QtWidgets.QApplication.processEvents()
                    save_API_n_results_to_txt(self.merchandise_name, self.mdse_infos, 2)
                else:
                    self.statusBar().showMessage(f"　第 {No} 件商品資訊爬蟲失敗")
                    #print("　第 {No} 件商品資訊爬蟲失敗")
            print(f"API-2 => Execution time: {time.time()-t1} sec\n")
            print(f"Total exec. time: {time.time()-firstAPI_exeTime} sec\n\n")
            '''
            Move the pictures directory of merchandises and two txt files to myPath
            '''
            # 3. 將同目錄下的暫存檔搬家(API-1 & API-2 results, merchandise pictures)
            self.imgsPath = move_mdseInfo_to_dest(self.merchandise_name)
            self.imgsPath += f"\{self.merchandise_name}_商品圖片"
        else:
            print("輸入不可為空")
    
    def sort_table(self, sorting_order, sorting_field):
        if self.dataSrc == "mdse_infos":
            self.mdse_infos.sort(key=lambda x:x[sorting_field], reverse=sorting_order)
        elif self.dataSrc == "favorites":
            # 對應到 DB 欄位, 因轉成tuple又以list傳回, 故需要用integer indexing
            db_fields = {"price_avg":6, "historical_sold":7, "stock":8, "liked_count":10} 
            index = db_fields[sorting_field]
            self.favorites.sort(key=lambda x:x[index], reverse=sorting_order)

    def sort_table_by_price_DESC(self):
        self.sort_table(True, "price_avg")
        self.update_table()
        
    def sort_table_by_price_ASC(self):
        self.sort_table(False, "price_avg")
        self.update_table()
        
    def sort_table_by_soldNum_DESC(self):
        self.sort_table(True, "historical_sold")
        self.update_table()
        
    def sort_table_by_soldNum_ASC(self):
        self.sort_table(False, "historical_sold")
        self.update_table()
        
    def sort_table_by_stock_DESC(self):
        self.sort_table(True, "stock")
        self.update_table()
        
    def sort_table_by_stock_ASC(self):
        self.sort_table(False, "stock")
        self.update_table()
        
    def sort_table_by_liked_count_DESC(self):
        self.sort_table(True, "liked_count")
        self.update_table()
        
    def sort_table_by_liked_count_ASC(self):
        self.sort_table(False, "liked_count")
        self.update_table()
        
    def setting_funcs(self, MainWindow):
        self.menu_1.triggered[QtWidgets.QAction].connect(self.menu_1_selected)
        
        self.btnQuery.clicked.connect(self.btnQuery_clicked)
        self.exit.triggered.connect(self.close)
        self.mdse_search.triggered.connect(self.reset_search)
        self.view_favorites.triggered.connect(self.update_table_withFavorites)
        self.sort_by_price_DESC.triggered.connect(self.sort_table_by_price_DESC)        
        self.sort_by_price_ASC.triggered.connect(self.sort_table_by_price_ASC) 
        self.sort_by_soldNum_DESC.triggered.connect(self.sort_table_by_soldNum_DESC)        
        self.sort_by_soldNum_ASC.triggered.connect(self.sort_table_by_soldNum_ASC)
        self.sort_by_stock_DESC.triggered.connect(self.sort_table_by_stock_DESC)        
        self.sort_by_stock_ASC.triggered.connect(self.sort_table_by_stock_ASC)
        self.sort_by_liked_count_DESC.triggered.connect(self.sort_table_by_liked_count_DESC)        
        self.sort_by_liked_count_ASC.triggered.connect(self.sort_table_by_liked_count_ASC) 
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PriceGo! 商品比價系統"))
        self.btnQuery.setText(_translate("MainWindow", "搜尋\n商品"))
        self.lbl_1.setText(_translate("MainWindow", "請輸入商品名稱："))
        self.lbl_2.setText(_translate("MainWindow", "搜尋結果："))
        self.menu_1.setTitle(_translate("MainWindow", "商品查詢"))
        self.menu_2.setTitle(_translate("MainWindow", "商品排序"))
        self.menu_3.setTitle(_translate("MainWindow", "追蹤商品"))
        self.menu_4.setTitle(_translate("MainWindow", "結束"))
        self.mdse_search.setText(_translate("MainWindow", "點我查詢"))
        self.sort_by_price_ASC.setText(_translate("MainWindow", "依 平均價格 排序(低>高)"))
        self.sort_by_price_DESC.setText(_translate("MainWindow", "依 平均價格 排序(高>低)"))
        self.sort_by_soldNum_DESC.setText(_translate("MainWindow", "依 銷量 排序(高>低)"))
        self.sort_by_soldNum_ASC.setText(_translate("MainWindow", "依 銷量 排序(低>高)"))
        self.sort_by_stock_ASC.setText(_translate("MainWindow", "依 庫存 排序(低>高)"))
        self.sort_by_stock_DESC.setText(_translate("MainWindow", "依 庫存 排序(高>低)"))
        self.sort_by_liked_count_ASC.setText(_translate("MainWindow", "依 喜歡次數 排序(低>高)"))
        self.sort_by_liked_count_DESC.setText(_translate("MainWindow", "依 喜歡次數 排序(高>低)"))
        self.view_favorites.setText(_translate("MainWindow", "查看追蹤商品"))
        self.exit.setText(_translate("MainWindow", "離開"))