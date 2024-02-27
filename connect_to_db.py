import db_conf
import mysql.connector

def db_connection():
    conf=db_conf.imp_config()
            
    dbconnection = mysql.connector.connect(user=conf[0],
                                        password=conf[1],
                                        host=conf[2],
                                        database=conf[3])
    return dbconnection