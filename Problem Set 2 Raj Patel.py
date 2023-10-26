#!/usr/bin/env python
# coding: utf-8

# ### Problem Set 2 -- Data Programming

# #### QUESTION 1 

# In[4]:


# Given python module
a = 0            # Assigning 0 to variable a.

def b():         # Defining function b  
 global a        # The above variable a is now declared as a global variable.

 a = c(a)        # Here we are passing a as an argument for function c,
                 # And assigning returning value of function c to variable a.  
        
def c(a):        # Defining function c which will required one argument.
 return a + 2    # returning provided argument + 2. 


# In[5]:


# Executing
b()
b()
b()
a


# ####  Elaboration of result.
# 
# So initially the value of a is 0,after that inside the function b we have declared a as an global variable.
# After declaring global we are assigning the returning value of function c(a) to a and since function c is taking a as an argument, return value of " a " increase by 2 according to increment logic of c.
# 
# So by the above logic we can say that if we are calling function b() one time the value of a incremented by 2. So after calling of function b() value of a=2, after second execution a=4 and after third execution value of a becomes 6. Which is what we are getting after executing just a. 

#  

# #### QUESTION 2

# In[13]:


def fileLength(File_Name):      # Defining filelength function which will return file length when correct name and path provided.
    try:
        Read_File = open(File_Name) 
        print(len(Read_File.read())) # getting the length of the file. 
    except FileNotFoundError:   # it will print this error message if file is not find through the directory
         print(f"Error:Please provide correct path and name of the file!")
    else:                       # or it will close the file 
        Read_File.close()


# In[14]:


# Working Example
fileLength("C:/Users/Raj Patel/Documents/College/Semester 2/Questions.txt")


# In[15]:


# Exception Example
fileLength("C:/Users/Raj Patel/Documents/College/Semester 2/uestions.txt")


# ##### Observation
# Here we can see that if the file path/name is not correct it will throw custom exception.

# #### QUESTION 3

# In[2]:


class Marsupial:            # class called Marsupial 
    def __init__(self):     # defining an objcet by using init 
        self.pouch = []     # creating an empty list to store results 

    def put_in_pouch(self, item):   # Here using put_in_pouch commanad to add iteams in our list called self.pouch
        self.pouch.append(item)

    def pouch_contents(self):
        return self.pouch


# In[18]:


class Kangaroo(Marsupial):        # A subclass called kangaroo. 
    
    def __init__(self, x, y):     # we have created object in it which can have two parameters in it
                                  # where x and y represents coordinates of kangaroo.
        super().__init__()
        self.x = x                
        self.y = y
    
    def jump(self, dx, dy):   #  jump method takes two argument dx and dy,which represents distance that kangaroo will be moving. 
        self.x = self.x + dx
        self.y = self.y + dy    
    
    def __str__(self):    
        return f"Kangaroo is at this location: ({self.x}, {self.y})"


# In[19]:


M = Marsupial() # object of marsupial class
M.put_in_pouch('Putting')
M.put_in_pouch('in the')
M.put_in_pouch('pouch')
print( M.pouch_contents())


# In[20]:


kangaroo_obj = Kangaroo(0,0) #initial location.

kangaroo_obj.put_in_pouch("I am from")

kangaroo_obj.put_in_pouch("kangaroo class")

print(kangaroo_obj)  

kangaroo_obj.jump(1,2)

print(kangaroo_obj)  


# # QUESTION 4

# In[1]:


def collatz(x):                   # Defining the function collatz 
        print(x)                  # Here we are using print function to pront starting point of collatz sequence. 
        if x == 1:                # The function will check if the x=1 then it will stop iteration and will exit the loop.
            return
        elif x % 2 == 0:          # If x is even number then it will call itself with argument x//2. 
            collatz(x // 2)
        else:
            collatz(3 * x + 1)    # else in case of odd number then it will call itself with argument 3*x+1.


# In[4]:


# Examples
collatz(1) 


# In[3]:


collatz(10)


# # QUESTION 5

# In[6]:


def binary_conversion(n):  # Function called binary_conversion to create binary data. 
    if n == 0:             # if the input is 0 it will return 0, same for 1 as well.
        return '0'
    elif n == 1:
        return '1'
    else:
        return binary_conversion(n // 2) + str(n % 2) # In other cases it divide input n by 2 and store that value to str till 0


# In[10]:


# Execution
print("Binary conversion of 4: " + binary_conversion(4))
print("Binary conversion of 9: " + binary_conversion(9))
print("Binary conversion of 2000: " + binary_conversion(2000))


# # QUESTION 6

# In[28]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):  #class HeadingParser as subclass of HTMLparser
    def __init__(self):
        super().__init__()
        self.indent = 0

    def handle_starttag(self, tag, attrs): # when start tag occurs while reading through file.
        if tag.startswith('h'):
            print(' '* self.indent, end='')
    
    def handle_data(self, data):
        print(data)
# testing implementation. here provided file was in .txt format so I have changed it to .html file.
infile = open('C:/Users/Raj Patel/Documents/College/Second Year/Ethan Davis/w3c.html')
content = infile.read()
infile.close()

hp = HeadingParser()
hp.feed(content)


# # QUESTION 7

# In[4]:


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

def webdir(url, length, indent):  # we have created the function called webdir 
    
        return


# In[5]:


webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)


# # QUESTION 8

# In[ ]:


# In order to gain information about weather data we first need to create a table that holds the information of the weather. 

import sqlite3  
conn = sqlite3.connect('weather.db')  # here we are establishing the connection with the dataset.
cursor = conn.cursor() # creating a cursor object with which we will perform the sql operations.

# with the help of cursor.execute query we are creating weather_data1 table.
cursor.execute('''                
    CREATE TABLE Weather_data1(
        City VARCHAR(15),       
        Country VARCHAR(15),
        Season VARCHAR(15),
        Temperature FLOAT,
        Rainfall FLOAT
    )
''')

# data to be isnserted into table.
weather_info = [('Mumbai', 'India', 'Winter', 24.8, 5.9),
    ('Mumbai', 'India', 'Spring', 28.4, 16.2),
    ('Mumbai', 'India', 'Summer', 27.9, 1549.4),
    ('Mumbai', 'India', 'Fall', 27.6, 346.0),
    ('London', 'United Kingdom', 'Winter', 4.2, 207.7),
    ('London', 'United Kingdom', 'Spring', 8.3, 169.6),
    ('London', 'United Kingdom', 'Summer', 15.7, 157.0),
    ('London', 'United Kingdom', 'Fall', 10.4, 218.5),
    ('Cairo', 'Egypt', 'Winter', 13.6, 16.5),
    ('Cairo', 'Egypt', 'Spring', 20.7, 6.5),
    ('Cairo', 'Egypt', 'Summer', 27.7, 0.1),
    ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)
]                                   

# inserting data into weather_data1 table
cursor.executemany('''
    INSERT INTO Weather_data1 (City, Country, Season, Temperature, Rainfall)
    VALUES (?, ?, ?, ?, ?)
''', weather_info)

conn.commit()  # here we use command queries to use the table and make it close 
conn.close()


# In[35]:


conn = sqlite3.connect('weather.db') #connecting with the database.
cursor = conn.cursor()

# task_a: All THE TEMPURETURE DATA
print(" ----------**---------- ")
cursor.execute("SELECT Temperature FROM Weather_data1")
temperature = cursor.fetchall()
for T in temperature:
    print("Temperature from all the city for all weather:")
    print(T)

# task_b: All THE CITIES BUT WITHOUT REPETITION
print(" ----------**---------- ")
cursor.execute("SELECT DISTINCT City FROM Weather_data1 ")
distinct_cities = cursor.fetchall()
for C in distinct_cities:
    print("City from the weather_data1 table:")
    print(C) 
        

# task_c:  All THE RECORDS OF INDIA 
print(" ----------**---------- ")
cursor.execute("SELECT * FROM Weather_data1  WHERE Country = 'India'") # giving country = India, this will fetch data from only India.
India_city = cursor.fetchall()
for I in India_city:
    print("Records of Indian city from the given data:")
    print(I)  
    
    
# Task_d:  All THE FALL RECORDS 
print(" ----------**---------- ")
cursor.execute("SELECT * FROM Weather_data1  WHERE Season = 'Fall'")
fall_record = cursor.fetchall()
for F in fall_record:
    print("All the fall Records from the givin data :")
    print(F)

# task_e: The city, country, and season for which the average rainfall is between 200 and 400 millimeters
print(" ----------**---------- ")
cursor.execute("SELECT City, Country, Season FROM Weather_data1 GROUP BY City, Country, Season HAVING AVG(Rainfall) BETWEEN 200 AND 400")
Ave_rainfall = cursor.fetchall()
for R in Ave_rainfall:
    print("city record where average rainfall is between 200 and 400 millimeters from givin data:")
    print(R)

# task_f: The CITY AND COUNTRY FOR which the average Fall temperature is above 20 degrees, in increasing temperature order
print(" ----------**---------- ")
cursor.execute("SELECT City, Country FROM Weather_data1  WHERE Season = 'Fall' GROUP BY City, Country HAVING AVG(Temperature) > 20 ORDER BY AVG(Temperature) ASC")
average_temp = cursor.fetchall()
for A in average_temp:
    print("Cities with Average Fall Temperature above 20 degrees, in increasing order for given data:")
    print(A)

# task_g: The TOTAL ANNUAL RAINFALL OF CIARO 
print(" ----------**---------- ")
cursor.execute("SELECT SUM(Rainfall) AS TotalRainfall FROM Weather_data1  WHERE City = 'Cairo'")
cairo_rain = cursor.fetchall()
print("Total Annual Rainfall for Cairo:", cairo_rain)

# task_h: The TOTAL RAINFALL OF THE SEASON
print(" ----------**---------- ")
cursor.execute("SELECT Season, SUM(Rainfall) AS TotalRainfall FROM Weather_data1  GROUP BY Season")
seasonal_rain = cursor.fetchall()
for S in seasonal_rain:
    print("Total Rainfall for Each Season:")
    print(S)
    
conn.close() #closing of the connection


# # QUESTION 9

# In[6]:


# First defining the list of words.
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']


# In[8]:


# Task 1 : printing all the words of the lists in uppercase. 
task_1 = []
for w in words:
    task_1.append(w.upper())

print(task_1)    


# In[9]:


# Task 2: printing all words to in lowercase.
task_2 = []
for w in words:
    task_2.append(w.lower())

print(task_2)    


# In[10]:


# task 3: Lengths of each word in list.
task_3 = []
for w in words:
    task_3.append(len(w))
print(task_3)


# In[23]:


# Task 4: the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and the length of the word.
task_4 = []
for w in words:
    combined_list = [w.upper(), w.lower(), len(w)]
    task_4.append(combined_list)

print(task_4)


# In[24]:


# Task 5: words from the lists with 4 or more characters
task_5 = []
for w in words:
    if len(w) >= 4:
        task_5.append(w)
print(task_5)


# In[ ]:




