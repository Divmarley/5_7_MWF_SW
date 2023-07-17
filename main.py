
# inbuilt 
# date

# import datetime
# json 
# todayDate = datetime.datetime.now()

# print("Today's date is : ", todayDate)


# print(todayDate.strftime("%b"))
# print(todayDate.strftime('%A'))
# print(todayDate.strftime('%a'))
# print(todayDate.strftime('%Y'))
# print(todayDate.strftime('%y'))
# print(todayDate.strftime('%H'))
# print(todayDate.strftime('%I'))
# print(todayDate.strftime('%I'))
# print(todayDate.strftime('%z'))
# print(todayDate.strftime('%m'))

import math
import json
import os

x = math.sqrt(25) 


# 2023/07/17 
# extenal
 

# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# } 
# k =json.dumps(x)
# print(type(k))



# passme = input("enter your password")


# myfile = open("data.txt","w")
# # print(myfile.readline())
# # print(myfile.readline()) 

# myfile.write(passme)



# os.remove('note.txt')

if os.path.exists("index.html"):
    print("file deleted!!")
else:
    print("file doesnt exist")



# int myNum = 15;
# System.out.println(myNum);


myNum = 15
print(myNum)