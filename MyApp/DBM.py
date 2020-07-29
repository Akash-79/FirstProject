import pymysql as p

def getConnect():
    serverName="localhost"
    userName="root"
    passw=""
    dbName="dj10to12r"
    return p.connect(serverName,userName,passw,dbName)

def addEmp(t):
    db=getConnect()
    cr=db.cursor()
    sql="insert into emp values(%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllEmp():
    db=getConnect()
    cr=db.cursor()
    sql="select * from emp"
    cr.execute(sql)
    fl=cr.fetchall()
    db.commit()
    db.close()
    return fl

def Empdelete(id):
    db=getConnect()
    cr=db.cursor()
    sql="delete  from emp where id=%s"
    cr.execute(sql,id)
    db.commit()
    db.close()


def selectEmpById(id):
    db=getConnect()
    cr=db.cursor()
    sql="select * from emp where id=%s"
    cr.execute(sql, id)
    fl=cr.fetchall()
    db.commit()
    db.close()
    return fl[0]

def EmpUpdate(t):
    db=getConnect()
    cr=db.cursor()
    sql="update emp set name=%s,contact=%s,address=%s where id=%s"
    cr.execute(sql, t)
    db.commit()
    db.close()