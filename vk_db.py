import mysql.connector

db = {'host': 'localhost',
      'user': 'vsearch',
      'password': 'vsearchpasswd',
      'database': 'vkbotDB',}

conn = mysql.connector.connect(**db)
cursor = conn.cursor()

def ins_CUR_DATE(values):
    
    REQ = """insert into cur_date
            values(%s,%s,%s)"""
    cursor.execute(REQ,values)
    conn.commit()
    
    
def ins_CUR_MONTH_from_CUR_DATE():

    print('__________________________insert__current___month_________________')
    REQ = """insert into cur_month (user_id,date,spent_time)
            select user_id,(%s) as date, sum(temp_session) from cur_date
            where (last_enter > %s and last_enter < %s)
            group by user_id""" % (d1,d1,d2)
    cursor.execute(REQ)
    conn.commit()

def show_CUR_DATE():

    print('__________________________show__current___date_________________')
    REQ = """select * from cur_date"""
    cursor.execute(REQ)
    for row in cursor.fetchall():
        print(row)
       
def show_CUR_MONTH():

    print('___________________________show__current_month_________________')
    REQ = """select * from cur_month"""
    cursor.execute(REQ)
    for row in cursor.fetchall():
        print(row)    

def delete(table):
    if(table == 'month'):
        print('_____________________________DELETE__FROM__MONTH___________________')
        REQ = """delete from cur_month"""
    elif(table == 'date'):
        print('_____________________________DELETE__FROM__DATE___________________')
        REQ = """delete from cur_date"""
    cursor.execute(REQ)
    conn.commit()

values = (10789009,9520365,600)
table = 'month'

d1 = 6485300
d2 = 6526923


#ins_CUR_DATE(values)
#delete(table)
#show_CUR_DATE()
#show_CUR_MONTH()
ins_CUR_MONTH_from_CUR_DATE()
show_CUR_MONTH()

cursor.close()
conn.close()
