import pymysql
from datetime import datetime

def writeDB(count):
    db = pymysql.connect("116.62.164.196", "root", "xxqx@2017mysql!@#", "CRM")

    cur = db.cursor()
    sql ="update orders set order_num='%i',createtime='%s'"%(count,datetime.now())

    try:
        cur.execute(sql)
        db.commit()
        print(datetime.now())
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        cur.close()
        db.close()

def queryOrder():
    db = pymysql.connect("116.62.164.196", "root", "xxqx@2017mysql!@#", "CRM")

    cur = db.cursor()
    sql ="select order_num from orders"

    try:
        cur.execute(sql)
        results = cur.fetchone()
        return results[0]
    except Exception as e:
        print(e)
    finally:
        cur.close()
        db.close()