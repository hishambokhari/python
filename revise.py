


# setting variables
# income = 50
# tax_rate = 0.1

# income_tax = income * tax_rate

# print (income_tax)

# strings 

# print("I'm a string")

# mystring = 'abcdefg'

# print(mystring[2])

# slicing

# mystring = 'hello man how are you'

# # print(mystring[:3]) #upto but not including

# # print (mystring[1:4]) # from 1 to 4

# # x = mystring.split(' ')
# # print(x)

# x = "Insert another string: {} Item two: {}".format(mystring, 'dog')
# print(x)


#lists - pythons form of arrays

# myList = [1,50,3,4]

# myList[1] = 2 # replacing in lists

# print(myList)
# print(myList[1]) # indexing

# print(len(myList)) #lngth of a list


# append

# Adds to the end of the list
# myList.append("New item") 


# myList.extend("8,9,10") # extends to the list
# print(myList)



# myList.pop() # removes last item from list
# print(myList)


# myList.reverse() # reverses the list
# print(myList)




# myList.sort() # sorts the list the list
# print(myList)


# matrix

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# first_col = [row[0] for row in matrix] # grabs first element in every list


# print(first_col)



# Dictionaires

my_stuff = {"key1":"value","key2":"value2","key3":{'123':[1,2,'grabme']}}

print(my_stuff["key3"]['123'][2])

my_food = {'lunch':'pizza','bfast':'eggs'}
my_food['lunch'] = 'burger'
my_food['dinner'] = 'pasta' # adding to the list
print(my_food)


