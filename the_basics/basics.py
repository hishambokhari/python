# # monday_temperatures = [9.1,8.8,7.5]

# # student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.9} 

# # mysum = sum(student_grades.values()) # to get the values of the dictionary just do this
# # # mysum = sum(student_grades.keys())  to get the keys of the dictionary just do this
# # length = len(student_grades)
# # mean = mysum/length
# # print(mean)

# # student_grades = [10.1,8.8,7.5,10.1,4.5,10.1] # student_grades is the list - list.count() returns the number of times 10.1 appeared 
# # print(student_grades.count(10.1))

# # name = "hisham"
# # print(name.lower()) # lower() for lowerclass and upper() for upper class


# # These are called tuples - with () brackets.
# # monday_temperatures = (1,4,5) # cannot append tuples
# # print(monday_temperatures)

# # monday_temperatures2 = [1,4,5]
# # monday_temperatures2.append(6)
# # monday_temperatures2.remove(4)  using remove() method to remove from the list
# # print(monday_temperatures2) # lists are appendable - using append() method to add to the list

# monday_temperatures = [9.1,8.8,7.5]

# # finding the index from the list using index() method
# print(monday_temperatures.index(8.8))



# functions in python
# def mean(mylist):
#     the_mean = sum(mylist)/len(mylist)
#     return the_mean     

# print(mean([2,4,6]))     # calling the function using print

# conditionals - if else statements

# def mean(n):
#                                                            # the_mean = sum(n)/len(n)
#   if type(n) == dict:
#     the_mean = sum(n.values())/len(n)
#   else:
#       the_mean = sum(n)/len(n)
#   return the_mean

# student_grades = { "mary":9.1,"sim":8.8,"john":7.5}
# monday_temperatures = [8.8,9.1,9.9]
# print(mean(monday_temperatures))

# x = -10
# if x * 2 > x:
#   print("Greater")
# else:
#   print("Less or Equal")

# def foo(x, array):
#   if x in array:
#     return True
#   else:
#     return False

# print(foo(1,[1,2,3])) # true
# print(foo(1,[2,3])) # false
# print(foo(1,['1',2,3]))  # false  

# def mean(n):
#   if isinstance(n, dict):
#     the_mean = sum(n.values)/len(n)
#   else:
#     the_mean = sum(n)/len(n)

#   return the_mean

# better to use isinstance instead of type(n) == dict:

# def foo(n):
#   if len(n) >= 8:
#     return True
#   else:
#     return False

# def temp(n):
#   if n > 7:
#     return "Warm"
#   else:
#     return "Cold"  
   
   # Elif

# def hish(x, y):
#   if x > y:
#     return("x is greater than y")
#   elif x == y:
#     return("x is equal to y")
#   else:
#     return("x is less than y") 

# print(hish(3,3))    


# User input
# user_input = input("Enter your name: ")
# message = "Hello %s!" % user_input -- This is how to formart a string (single variables)
# print(message)

# Multiple inputs
# name = input("Enter your name: ")
# surname = input("Enter your surname: ")

# message = "Hello %s %s" % (name, surname)
# print(message)

# def foo(name):
#   return "Hi %s" % name

# print(foo("Hisham"))  

# def foo(name):
#   return "Hi %s" % name.capitalize()


# print(foo("hisham"))  


# For loops

# monday_temperatures = [9.1,8.8,7.6]

# for temp in monday_temperatures:
#   print(round(temp)) # round() method is used to round of the numbers. Temp is a variable that can be named anything

# colors = [11,34,98,43,45,54,54]

# for items in colors:
#   if items > 50:
#     print(items)

# colors = [11,34.1,98.2,43,45.1,54,54] # checking for items to be an int and > 50 using the int() and the 'and' operator.
# for items in colors:
#   if items == int(items) and items > 50:
#     print(items)


    