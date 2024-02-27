import json

def imp_config():
    with open('C:/Python_projects/New_projects/db_config.json', 'r') as file:
        data = json.load(file)
        print(data)
        conf_user=(data['user'])
        conf_password=(data['password'])
        conf_host=(data['host'])
        conf_db=(data['database'])
        return conf_user, conf_password, conf_host, conf_db
    # for item in data:
    #     print(item[user])