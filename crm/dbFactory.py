import pymysql

class dbFactory(object):
    def __init__(self,host,loginname,password,db):
        self.host = host
        self.loginname = loginname
        self.password = password
        self.db = db
        print("初始化...")

    def __get_connect(self):
        try:
            db = pymysql.connect(self.host, self.loginname, self.password, self.db,charset="utf8")
            return db
        except Exception as e:
            print("初始化数据库连接失败...",e)

    def exeQuery(self,sql):
        db = self.__get_connect()
        re = []
        try:
            cur = db.cursor()
            cur.execute(sql)

            results = cur.fetchall()

            for row in results:
                username = row[0]
                sex = row[1]
                age = row[2]
                address = row[3]
                password = row[4]

                re.append((username,password,sex,age,address))
        except Exception as e:
            print("查询失败,原因：", e)
        finally:
            db.close()

        return re

    def exeUpdate(self,sql):
        db = self.__get_connect()
        try:
            cur = db.cursor()
            cur.execute(sql)

            db.commit()

        except Exception as e:
            db.rollback()
            print("失败,原因：", e)
            return False;
        finally:
            db.close()

        return True

#c = dbFactory("116.62.164.196","root","xxqx@2017mysql!@#","CRM")
#data  = c.exeQuery("select username,sex,age,address,password from user")
#print(data)
