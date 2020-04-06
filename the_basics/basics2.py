# myfile = open("fruits.txt") # create a file[]
# content = myfile.read()
# myfile.close() # used to close a file

# with open("files/veg.txt", "w") as myfile: #used to create a new file
#   myfile.write("Tomato\nCucumber\nOnion\n")
#   myfile.write("garlic")

# import time
# import os

# while True:
#   if os.path.exists("files/veg.txt"):
#     with open("files/veg.txt") as file:
#       print(file.read())
#   else:
#     print("File does not exist.")    
     
#   time.sleep(5) # freezes script execution for 5 seconds


# Third party modules: Pandas

import time
import os
import pandas

while True:
  if os.path.exists("files/temps_today.csv"):
    data = pandas.read_csv("files/temps_today.csv")
    print(data.mean()["st1"])
  else:
    print("File does not exist.")    
     
  time.sleep(10) # freezes script execution for 10 seconds
