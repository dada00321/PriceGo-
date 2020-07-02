import glob
import os
import shutil
import time

def save_API_n_results_to_txt(mdse_name, src_list, API_n):
    '''
    The first time saving regarding to the results of API-1 & API-2,
    would operating in the outer layer directory (same as the GUI and scrapy program)
    '''
    if API_n == 1:
        save_path = f"{mdse_name}.txt"
    elif API_n == 2:
        save_path = f"{mdse_name}_商品資訊.txt"
    with open(save_path, 'w', encoding="utf-8") as fp:
        msg = ""
        for info in src_list:
            for key, value in info.items():
                msg += f"{key}: {value}\n"
            msg += "\n"
        print(f"txt檔: {save_path}", end=' ')
        try:
            fp.write(msg)
            print("寫入成功！\n", "="*25, sep='')
        except:
            print("寫入失敗\n", "="*25, sep='')

def build_dest_env(mdse_name, dest_dir):
    '''
    Constructing storing environment  (destination path: myPath)
    '''
    myPath = ""
    myPath += dest_dir
    if not os.path.exists(myPath):
        os.mkdir(myPath)
        
    myPath += f"\{mdse_name}"
    if not os.path.exists(myPath):
        os.mkdir(myPath)
    
    t = time.localtime()
    curr_mdse_dir = "\{}_{}_{:02d}_{:02d}_{:02d}_{:02d}".format(mdse_name, t[0], t[1], t[2], t[3], t[4])
    myPath += curr_mdse_dir
    if not os.path.exists(myPath):
        os.mkdir(myPath)
    return myPath
    
def move_mdseInfo_to_dest(mdse_name):
    dest_dir = "repository" # parent directory of all sort of categories
    '''
    Move files which in outer layer to 'myPath'
    '''
    files = [f"{mdse_name}_商品圖片", f"{mdse_name}.txt", f"{mdse_name}_商品資訊.txt"]
    existing_files = [file for file in files if file in glob.glob("*")]
    avaiable_count = len(existing_files)
    if 0 < avaiable_count <= 3:
        if avaiable_count == 3:
            print("商品資訊檔案全數存在, 正在搬家")
        elif 0 < avaiable_count < 3:
            print("商品資訊檔案有部分遺失, 正在搬家")
        myPath = build_dest_env(mdse_name, dest_dir) # myPath: 新家地址
        move_failed = False
        for file in files:
            #print(f"Yes, {file}")
            try:
                shutil.move(file, myPath)
            except:
                move_failed = True
                print("商品暫存檔搬家失敗: 執行shutil.move()方法時發生錯誤")
        if not move_failed:
            print("商品暫存檔搬家成功")
        return myPath
        
    elif avaiable_count == 0:
        print("商品資訊檔案全數遺失, 搬移操作中斷")
        return None
    else:
        print("有先前殘留的未搬移檔案, 搬移操作中斷")
        return None
