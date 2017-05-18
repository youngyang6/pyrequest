import pymysql.cursors
import os
import configparser as cparser

#===========Reading db_config.ini setting===================
base_dir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/db_config.ini"
print (file_path)

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
db = cf.get("mysqlconf","db_name")

#===========Mysql base operating============
class DB:
    def __init__(self):
        try:
            #connect database
            self.connection = pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            port=int(port),
                                            db=db,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print ("Mysql error %d: %s" % (e.args[0],e.args[1]))

    #clear data
    def clear(self,table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    #insert sql
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO "+ table_name +" (" + key + ") VALUES (" + value + ")"
        print (real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    #close database
    def close(self):
        self.connection.close()


if __name__ == '__main__':

    db = DB()
    table_name = "sign_event"
    data = {'id':1,'name':'苹果8','`limit`':2000,'status':1,'address':'济南奥体中心','start_time':'2017-06-30 18:30:00'}

    #table_name = "sign_guest"
    #data2 = {'realname':'billy','phone':18612345678,'email':'186186@example,com','sign':0,'event_id':1}

    db.clear(table_name)
    db.insert(table_name,data)
    db.close()
