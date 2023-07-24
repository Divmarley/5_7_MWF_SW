import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user ="root",
    password ="",
    database = "python_mwf_57"
)

# print(mydb)

myCursor = mydb.cursor()


# myCursor.execute("SHOW DATABASES")

# for database in myCursor:
#     print(database)
    
# creating database
# myCursor.execute("CREATE DATABASE python_mwf_57")

# creating table
# myCursor.execute("CREATE TABLE  users(id INT, name VARCHAR(200) )")



# INSERT DATA INTO the user
# myCursor.execute("INSERT INTO users(id,name) VALUES (1,'marley')")

# mydb.commit()


# another ways 
# sql = "INSERT INTO users(id,name) VALUES (%s,%s)"
# val = [
#     (4,'ama'),
#     (5,'nii')
# ]
# myCursor.executemany(sql,val)

# mydb.commit()

# print(myCursor.rowcount,"data was inserted ")


# select all data from table 

myCursor.execute("SELECT * FROM users ")

myresult = myCursor.fetchall()

for user in myresult:
    print(user)



# select a particular data from table 
myCursor.execute("SELECT * FROM users WHERE name ='randy'")

myresult = myCursor.fetchall()

for user in myresult:
    print(user)