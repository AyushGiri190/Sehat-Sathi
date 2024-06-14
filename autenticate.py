import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="giriayush190@",
    database = "user_login"
)
cursor = mydb.cursor()

def signup(email,password):
    query = 'insert into info values(%s,%s)'
    values = (email,password)
    try:
        cursor.execute(query,values)
        mydb.commit()
    except:
        print("wrong entry")
 
def signin(email,password):
    query = 'select * from info where email=%s and password=%s'
    values = (email,password)

    cursor.execute(query,values)
    result = cursor.fetchall()
    if len(result)==0:
        return 0
    else :
        return 1
def check_mail(email):
    query = 'select * from info where email=%s and 1=%s'
    num=1
    value = (email,num)

    cursor.execute(query,value)
    result = cursor.fetchall()
    if len(result)==0:
        return 0
    else :
        return 1