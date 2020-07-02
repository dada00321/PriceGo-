import pymysql
import re
#from sqlalchemy.exc import IntegrityError
import warnings

# suppress all warnings
''' 當第一次出現某db已存在dbms,且欲執行create db的command時,
儘管SQL中有 'IF NOT EXISTS', 仍會出現 warning:
Warning: (1007, "Can't create database 'db_阿薩姆雙茶會烏龍奶茶'; database exists")
'''
warnings.filterwarnings("ignore")

''' for this program: '''
#from cfg_assistant import get_DB_config
''' for GUI program: '''
from modules.cfg_assistant import get_DB_config 

def mdfy_db_mdse_name(mdse_name): # modify the merchandise name of database
    mdse_name = mdse_name.replace(" ", "_")
    pattern = "[^a-zA-Z0-9\u4e00-\u9fa5_]"
    mdse_name = re.sub(pattern, "", mdse_name)
    return mdse_name

def connect_db(db_name=""):
    db_account, db_passwd = get_DB_config()[0], get_DB_config()[1]
    try:
        db = pymysql.connect("localhost", db_account, db_passwd, db_name, charset="utf8")
        #print("Scuuessfully connect database!")
        return db
    except:
        print("Fail to connect database...")
        print("請檢查本地伺服器是否開啟...")
        return None

def view_db(mdse_name):
    mdse_name = mdfy_db_mdse_name(mdse_name)
    db_name, table_name = f"db_{mdse_name}", f"tbl_{mdse_name}"
    db = connect_db(db_name)
    if db != None:
        cursor = db.cursor()
        
        # 1. 指向該商品資料庫
        sql = f"USE {db_name};"
        cursor.execute(sql)
        #print("Process 1 OK!") # for test
        
        # 2. 從該商品 table 中, fetch 全部資料
        sql = f"""SELECT * FROM {table_name}
                  ORDER BY `No`"""
        cursor.execute(sql)
        #print("Process 2 OK!") # for test
        
        records = cursor.fetchall() # type: tuple
        '''
        for record in records:
            print("No:", record[0])
            print("name:", record[3][:10]+"...")'''
        # Turns double-layer tuple to double-layer list
        records = [list(data) for data in records]
        return records
        
def save2db(mdse_name, values):
    mdse_name = mdfy_db_mdse_name(mdse_name)
    db = connect_db()
    if db != None:
        cursor = db.cursor()
        
        # 1. 以搜尋之商品名稱，建立資料庫(若尚未存在)
        sql = "CREATE DATABASE IF NOT EXISTS db_商品名稱;".replace("商品名稱", mdse_name)
        cursor.execute(sql)
        #print("Process 1 OK!") # for test
         
        # 2. 指向該商品資料庫
        sql = "USE db_商品名稱;"
        sql = sql.replace("商品名稱", mdse_name)
        cursor.execute(sql)
        #print("Process 2 OK!") # for test
        
        # 3. 以搜尋商品名稱，建立資料表(若尚未存在)
        sql=  """CREATE TABLE IF NOT EXISTS tbl_商品名稱 ( 
                    No INT(10) UNSIGNED NOT NULL PRIMARY KEY,
                    itemid BIGINT(11) UNSIGNED DEFAULT NULL,
                    shopid INT(10) UNSIGNED DEFAULT NULL,
                    name VARCHAR(60) DEFAULT NULL,
                    price_max MEDIUMINT(8) UNSIGNED DEFAULT NULL,
                    price_min MEDIUMINT(8) UNSIGNED DEFAULT NULL,
                    price_avg MEDIUMINT(8) UNSIGNED DEFAULT NULL,
                    historical_sold MEDIUMINT(8) UNSIGNED DEFAULT NULL,
                    stock MEDIUMINT(8) UNSIGNED DEFAULT NULL,
                    location VARCHAR(20) DEFAULT NULL,
                    liked_count MEDIUMINT(6) UNSIGNED DEFAULT NULL,
                    brand VARCHAR(20) DEFAULT NULL,
                    image VARCHAR(32) DEFAULT NULL,
                    description VARCHAR(250) DEFAULT NULL
                ) ENGINE=MyISAM DEFAULT CHARSET=utf8;"""
        sql = sql.replace("商品名稱", mdse_name)
        #print(f"create-table-SQL:\n{sql}")
        cursor.execute(sql)
        #print("Process 3 OK!") # for test
        
        # 4. 新建一筆資料(但SQL沒有判斷存在與否的syntax，需補抓例外:IntegrityError)
        ''' 當該資料的 Primary Key 被註冊過時，會發生以下錯誤:
        IntegrityError(1062, "Duplicate entry '1' for key 'PRIMARY'")
        '''
        sql = """INSERT INTO `tbl_商品名稱` (`No`,`itemid`,`shopid`,`name`,`price_max`,`price_min`,
                `price_avg`,`historical_sold`,`stock`,`location`,`liked_count`,
                `brand`,`image`,`description`)
                VALUES (商品紀錄);"""
        sql = sql.replace("商品名稱", mdse_name)
        sql = sql.replace("商品紀錄", values)
        try:
            cursor.execute(sql)
            #print("Process 4 OK!") # for test
            db.commit()
            print("成功加入追蹤清單！")
        #except IntegrityError:
        except:
            print("該商品已列入追蹤清單")
            #print(f"insert-SQL:\n{sql}")
        db.close()