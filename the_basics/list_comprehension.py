# creating lists - list comprehension
# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

# temps = [221, 234, 340, -999, 230] # How to exclude -999 from the list of temps

# new_temps = [temp/ 10 for temp in temps if temp != -999]

# print(new_temps)

# something = [99, 'no data', 95, 94, 'no data']

# only_numbers = [numbers for numbers in something if numbers != "no data"]

# print(only_numbers)

# def foo(lst): 
#   return [numbers for numbers in lst if not isinstance(numbers, str)]

# print(foo([99, 'no data', 95, 94, 'no data']))   This is the correct way to do it

# def foo(lst):
#   return [numbers for numbers in lst if numbers > 0]

# print(foo([-5, 3, -1, 101]))  

# list comprehension where 0 is output instead of -999

# temps = [221, 234, 340, -999, 230]

# new_temps = [temp / 10 if temp != -999 else 0 for temp in temps] useful when doing if/else inside a list

# print(new_temps)

# def foo(lst):
#   return [zero if not isinstance(zero, str) else 0 for zero in lst]

# print(foo([99, 'no data', 95, 94, 'no data']))  

# def foo(lst):
#   return sum([float(i) for i in lst])



# print(foo(['1.2', '2.6', '3.3']))  
