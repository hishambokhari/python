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

def mean(n):
                                                           # the_mean = sum(n)/len(n)
  if type(n) == dict:
    the_mean = sum(n.values())/len(n)
  else:
      the_mean = sum(n)/len(n)
  return the_mean

student_grades = { "mary":9.1,"sim":8.8,"john":7.5}
monday_temperatures = [8.8,9.1,9.9]
print(mean(monday_temperatures))