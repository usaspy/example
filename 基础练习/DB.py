import pymysql
from datetime import datetime

def connect():
    db = pymysql.connect("116.62.164.196","root","xxqx@2017mysql!@#","xxqx")

    cur = db.cursor()

    sql = "insert into SYS_ROLE(ID,NAME,ENABLE,DESCRIBLE,CREATETIME)VALUES('%s','%s','%s','%s','%s')"% ('U001','zhanghong','1','test',datetime.now())

    try:
        cur.execute(sql)
        db.commit()
        print("添加数据完成")
    except Exception as e:
        print("insert fail,case:%s"% e)
        db.rollback()
    finally:
        db.close()

def main():
    connect()

if __name__ == "__main__":
    main()