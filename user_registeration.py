# pip install mysql-connector-python
# pip install bcrypt
import mysql.connector 
import bcrypt

mydb =mysql.connector.connect(
    user="root",
    host="localhost",
    password= "",
    database="registration"
)

myCursor = mydb.cursor()

# create database
# myCursor.execute("CREATE DATABASE registration")

# create table
# myCursor.execute("CREATE TABLE users(id INT, name VARCHAR(200), email VARCHAR(255),password VARCHAR(400))")

# insert into user table


id_data=input("enter you id number :")
name_data= input("enter your name :")
email_data =input("enter your email :")
password_data = input("enter your password :")

 

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_data.encode(), salt)


def create_user():
    sql="INSERT INTO users(id, name, email, password) VALUES (%s,%s,%s,%s)"
    val = id_data,name_data,email_data,hashed
    myCursor.execute(sql,val)

    mydb.commit()

create_user()
