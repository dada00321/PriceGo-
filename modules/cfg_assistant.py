import configparser

def get_DB_config():
    config = configparser.ConfigParser()
    
    ''' for this program: '''
    #cfg_path = r"../res/db_cfg/db_cfg.ini"
    
    ''' for GUI program: '''
    cfg_path = r"./res/db_cfg/db_cfg.ini"
    
    config.read(cfg_path, encoding="utf-8")
    items = config.items(config.sections()[0])
    return [items[0][1][1:-1], items[1][1][1:-1]]