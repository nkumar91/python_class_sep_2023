import mysql.connector as con
host = "localhost"
user = "root"
password = ""
db_name = "python_connect"

connect = con.connect(host=host,user=user,passwd=password,database=db_name)
cur=connect.cursor()


#FOR INSERTING DATA
# name = "Akash"
# email = "Akash@u.com"
# password = "1234"

# SQL = "insert into account(name,email,password) VALUES(%s,%s,%s)"

# val=(name,email,password)

# cur.execute(SQL,val)
# connect.commit()


# FOR READ DATA

# SQL = "SELECT * FROM account WHERE email = %s and password = %s"
# val = ('Akash@u.com','1234')
# cur.execute(SQL,val)
# list  = cur.fetchall()  # fetchone
# print(list)

# try:
#     for m in list:
#         print(m[0],m[1])
# except Exception as E:
#      print(list[0],list[1])

