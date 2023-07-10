# '''this is to display my name
# name jjfvkdfgkgld
# grgndfkgkgdflmg
# dskfmskldnmsf '''

# """  """
# # print("marley's")

# # print('sika')

# # x =4
# # y = 5

# # print(x+y)


# # personName = "marley"
# # personPhonenumber = 6544564564
# # personWeight = 22.54
# # _isAlive_ = True
# # isFemale = False


# # # print(type(personName))
# # print(type(personPhonenumber))


# #DATA TYPES
# # STRING  "" ''
# # string = "qwertyuiop"

# # print("a")
# # print(type(string))


# # personName = ('nana addo' ,'jfdjfdhkjgn')
# # print(type(personName))
# # print("hello"+ ' ' +personName[0:3])

# # FLOAT 342432.454 -453.45
# # print(23.233 +233.3)
# # INTEGER  4564  -454
# # BOOLEAN  True or False


# # LIST   []
# # TUPLES  ()
# # DICT  {}
# # SET  {'a',}


# # mylist = ["apple", "banana", "cherry", "cherry"]

# friendOne ='kofi'
# friendTwo ='ama'
# friendThree ='kojo'

# # print(friendTwo)
# friends =['kofi','ama','kojo']
# # print(friends)
# # print(type(friends))

# # print(len(friends))

# # print('my first friend is called' , friends[0])
# # print(friends[2])
# # print(friends[1:2])
# # print(friends[:2])


# fruits = [
#     'apple', 'banana'
# ]


# # print first 20 fruits
# # print(len(fruits[:20]))

# # length of items in our fruits varaible

# # check the datatype of the fruits varaible


# # print(fruits[-2])


# """

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.


# """
# # print(fruits)
# # fruits[-1] = 'Ghana'
# # print(fruits)


# # fruits[0:5] = ["***","***","***","***","***"]

# # fruits.insert(2,"qwerty")
# # fruits.append('gari')
# # fruits.append('x')
# # print(fruits)


# # thislist = ["apple", "banana", "cherry","apple"]
# # tropical = ["mango", "pineapple", "papaya"]

# # print(tropical+thislist)

# # thislist.extend(tropical)


# # thislist.remove("apple")
# # thislist.pop(0)
# # thislist.pop(0)
# # thislist.clear()
# # del thislist


# # print(thislist)


# #  Python - Update Tuples
# # fruits= ("apple", "banana", "cherry","mango", "pineapple", "papaya")

# # convert tuple into a list
# # newFruitlist  = list(fruits)

# # newFruitlist[2]= "kiwi"
# # # print(type(x))

# # newFruittuple = tuple(newFruitlist)

# # print(newFruittuple)


# # Python - Unpack Tuples
# # When we create a tuple, we normally assign values to it.
# #  This is called "packing" a tuple:


# fruits = (
#     'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
#     'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
#     'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
#     'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
#     'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
#     'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
#     'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
#     'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
#     'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
#     'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
#     'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
#     'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
#     'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
#     'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
#     'watermelon', 'xigua', 'yangmei', 'zucchini'
# )

# # bad ways
# # a = fruits[0]
# # b = fruits[1]
# # print(a)
# # print(b)
# # (x,*Y,y,X) = fruits


# # Using Asterisk*
# # If the number of variables is less than the number of values,
# #  you can add an * to the variable name and the values will be assigned to the variable as a list:

# # good approach
# # (a ,*b,c) = fruits

# # print(a)
# # print(b)


# # print(fruits.count("banana"))
# x = fruits.index("tangerine")
# print(x)


# fruits= {1}


# # fruits.pop()
# # fruits.pop()
# # fruits.pop()
# # fruits.pop()
# # fruits.pop()
# # fruits.pop()
# # fruits.remove("apple")
# # fruits.remove("cherry")
# # fruits.clear()
# print(type(fruits))


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*,
# changeable and do not allow duplicates.


car = {"name": "BMW", "color": "red"}

# print(type(car))
# print(car)
# print(car["1"])
# print(car["color"])

# car["year"]=2023
# print(len(car))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# my_list = [1, 2, 3, 4, 5]
# my_list.sort()

# # my_list.reverse()

# print(my_list)


# def name_function():
#     print('hello')


# name_function()


# def name_function():
#     return 'hello'

# print(name_function())


# def display_name(name):
#     print(name)


# display_name()


# def calc_age(currentYear,yearBorn):
#     return  currentYear-yearBorn

# print(calc_age(2024,1957))
# print(calc_age(2024,1992))
# print(calc_age(2025,1990))


# def twitter_username_gen(yourname):
#     return '@'+yourname

# print(twitter_username_gen('sika'))
# print(twitter_username_gen('marley'))


# (h**2)/m
# (h*h)/m


# def calculate_BMI(height=0,weight=1):
#     return (height*height)/weight

# print(calculate_BMI(1.60,30))
# print(calculate_BMI(2.3,50))

# def list_children( *children):
#     return children[-1]


# print(list_children('jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
#     'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
#     'watermelon', 'xigua', 'yangmei', 'zucchini'))


# print(list_children('crownie',"maley",'eric'))


# A Quick Recap
# Let's quickly summarize what we've covered. In this tutorial, we've learned:

# how to define functions,
# how to call functions,
# how to pass in arguments to a function,
# how to create functions with default and variable number of arguments, and
# how to create a function with return value(s).


# def display_name( yourName="a" ):
#     return "hello" +  " "+ yourName[-1]

# print(display_name())

# def display_greet(greet):
#     return greet

# print(display_greet("good morning"))
# print(display_greet("good afteroon "))


# lambda function

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# display_greet = lambda greet,name : greet + " "+ name

# print(display_greet("good morning" ,'kofi'))
# print(display_greet("good afternoon",'ama'))


# def cal_age(currentYear,yearBorn):
#     age = currentYear - yearBorn
#     return age

# cal_age()

# x = lambda currentYear,yearBorn :   currentYear - yearBorn

# x()


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# print(x+ y)
# print(x - y)
# print(x / y)
# print(x * y)
# print(x // y)
# print(x ** y)


# Python Assignment Operators

# y = 50
# x = 10
# y = 50

# x+=y
# x-=y  # x = x - y
# x*=y  # x = x * y
# x/=y  # x = x / y
# x **=y  # x = x ** y
# x %=y  # x = x % y

# y += x #y = y+x
# print(y)

x = 90
y = 50

# print(x == y) #Equal
# print(x != y) #not Equal #output boolean
# print(x > y) #Greater than #output boolean
# print(x < y) #less than #output boolean

# print(5 > 10 or  10 < 10)


y = 40
x = 19
const = 18

# if (x > const):
#     print("Enter club")
# else:
#     print("go home")


email_bd = "kofikumi64@gmail.com"
password_bd = "passme123"
phone_db = "0244404044"
username_db = "@marley"

input_email = "kofikumi64@gmail.comd"
input_password = "passme123"
input_phone = "0244404044"
input_username = "@marley2"

# if (input_email == email_bd):
#     print("email is correct proceed")
# else:
#     print("email is not correct try again")

# if (input_password == password_bd):
#     print("password is correct proceed")
# else:
#     print("password is not correct try again")


# if (input_email == email_bd and input_password ==password_bd):
#     print("login")
# else:
#     print("not correct try again")


# if (input_email == email_bd or input_phone==phone_db or input_username==username_db):
#     if(input_email == email_bd):
#         print(f"email was used  {input_email}")
#         print("proceed to enter your password")
#         if (input_password ==password_bd):
#             print("login")
#     elif(input_phone==phone_db):
#         print(f"phone number was used  {input_phone}")
#         print("proceed to enter your password")
#         if (input_password ==password_bd):
#             print("login")
#     elif( input_username==username_db):
#         print(f"username was used  {input_username}")
#         print("proceed to enter your password")
#         if (input_password ==password_bd):
#             print("login")
# else:
#     print("not correct try again")

# openlabs@rrc


# a = 200
# b = 33


# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


# print("b is greater than a") if b > a else print("b is not greater than a")


# thislist = ["apple", "banana", "cherry"]

# if "banana" in thislist:
#     print('yes')
# else:
#     print("no")


# Loops

# fruits = (
#     'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
#     'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
#     'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
#     'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
#     'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
#     'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
#     'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
#     'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
#     'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
#     'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
#     'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
#     'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
#     'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
#     'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
#     'watermelon', 'xigua', 'yangmei', 'zucchini'
# )

# bad
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])


# for x in fruits:
#     print(x )


# print(range(6))
# for x in range(2,6):
#     pass


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

personalInfor = [
    {
        "name": "marley",
        "age": 20,
        "address": {
            "country": "Ghana",
            "zip_code": "+233",
            "phoneNumbers": [7777777, 900000],
        },
        "gender": "male",
        "occupation": ("developer"),
    },
]


# personalInfor[0]['occupation'] ="dancer"
# print(personalInfor)


# personalInfor[0]["address"]["phoneNumbers"] = tuple(personalInfor[0]["address"]["phoneNumbers"])
# print(personalInfor)


# r ={"phoneNumbers": [7777777,  900000 ]}

# r["phoneNumbers"]=(7777777,  900000 )
# print(r)


# class and objects
print()


# class Person():
#   # properties
#   def __init__(self,paraName,paraColor,pheight,pGender):
#     self.name = paraName
#     self.color= paraColor
#     self.height=pheight
#     self.gender = pGender

#   # method
#   def can_talk(self):
#     return 'i can talk'

# obj = Person("marley","red",5.99,"male")
# obj2 = Person("ama","yellow",2.99,"female")
# obj3 = Person()
# obj4 = Person()


# print(obj.name)
# print(obj.color)
# print(obj.height)
# print(obj.gender)
# print("=======================================")


# print(obj2.name)
# print(obj2.color)
# print(obj2.height)
# print(obj2.gender)


class Human:
    # properties
    def __init__(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height

    # method
    def can_talk(self):
        return f"{self.name} can talk"
    
    # create method for email using a default domaim marley@gmail.com 
    # or kwame@gmail.com


firstHuman = Human("marley", "red", 2.00)
print("firstHuman name:", firstHuman.name)
print("firstHuman color:", firstHuman.color)
print("firstHuman color:", firstHuman.color)
print("firstHuman can_talk:", firstHuman.can_talk())

secHuman = Human("kwame", "black", 10.55)
print("secHuman:", secHuman.name)
print("secHuman can_talk:", secHuman.can_talk())

 
class Animal(Human):
    pass

obj1 = Animal('kiki','red',6.7)

print(obj1.can_talk())