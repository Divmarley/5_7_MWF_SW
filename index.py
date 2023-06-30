


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


fruits = (
    'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
    'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
    'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
    'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
    'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
    'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
    'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
    'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
    'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
    'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
    'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
    'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
    'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
    'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
    'watermelon', 'xigua', 'yangmei', 'zucchini'
) 

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



car = {
    "name": "BMW",
    "color":"red"
}

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
 
def list_children( *children):
    return children[-1]


print(list_children('jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
    'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
    'watermelon', 'xigua', 'yangmei', 'zucchini'))


print(list_children('crownie',"maley",'eric'))