#!/usr/bin/env python
# coding: utf-8

# # Question 1

# Variable a is defined as 0. Enters b() block in which c(a) is now 0 which returns as a+2=2. Repeats the step which becomes 6.

# In[ ]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2 


# In[2]:


b()
b()
b()
a


# # Question 2

# In[12]:


def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))
    except:
        print("File "+file_name+" not found.")
        
file_length("Midterm.py")
file_length("idterm.py")


# # Question 3

# In[25]:


class Marsupial:                
    
    def __init__(self,x,y):       
        self.pouch=[]                   
             
    def put_in_pouch(self,items):   
        self.pouch.append(items)
        
    def pouch_contents(self):           
        return self.pouch



class Kangaroo(Marsupial):         
    def __init__(self,x,y):              
        super().__init__(x,y)     
        self.dx = 0                      
        self.dy = 0                        
    
    def jump(self,x,y):                 
        self.dx = self.dx + x    
        self.dy = self.dy + y
    
    def __str__(self):          
        
        return ('I am a Kangaroo located at coordinates ({} ,{})'.format(self.dx,self.dy))



k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()
print(k.pouch)  
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# # Question 4

# In[17]:


def collatz (x):
    if(x != 1):
        print(x )
    if(x == 1):
        print(x )
        return x
    if(x%2 == 0):
        x = x // 2
        collatz(x)
    else:
        x= 3*x + 1
        collatz(x)


# In[18]:


collatz(1)
collatz(10)


# # Question 8

# In[34]:


import sqlite3
conn = sqlite3.connect('forecast.db')
conn.execute('''
CREATE TABLE frcast(city string,
                      country string,
                      season string,
                      temperature integer,
                      rainfall integer);''')
conn.commit()
a = conn.cursor()
conn.execute("INSERT INTO frcast VALUES('Mumbai', 'India', 'Winter', 24.8, 5.9);")
conn.execute("INSERT INTO frcast VALUES('Mumbai', 'India', 'Spring', 28.4, 16.2);")
conn.execute("INSERT INTO frcast VALUES('Mumbai', 'India', 'Summer', 27.9, 1549.4);")
conn.execute("INSERT INTO frcast VALUES('Mumbai', 'India', 'Fall', 27.6, 346.0);")
conn.execute("INSERT INTO frcast VALUES('London', 'United Kingdom', 'Winter', 4.2, 207.7);")
conn.execute("INSERT INTO frcast VALUES('London', 'United Kingdom', 'Spring', 8.3, 169.6 );")
conn.execute("INSERT INTO frcast VALUES('London', 'United Kingdom', 'Summer', 15.7, 157.0);")
conn.execute("INSERT INTO frcast VALUES('London', 'United Kingdom', 'Fall', 10.4, 218.5);")
conn.execute("INSERT INTO frcast VALUES('Cairo', 'Egypt', 'Winter', 13.6, 16.5);")
conn.execute("INSERT INTO frcast VALUES('Cairo', 'Egypt', 'Spring', 20.7, 6.5);")
conn.execute("INSERT INTO frcast VALUES('Cairo', 'Egypt', 'Summer', 27.7, 0.1);")
conn.execute("INSERT INTO frcast VALUES('Cairo', 'Egypt', 'Fall', 22.2, 4.5);")



a.execute("SELECT temperature from frcast")
b=a.fetchall()             
for i in b:
  print(i, end="")



print()
a.execute("SELECT DISTINCT(city) from frcast")
b = a.fetchall()
for i in b:                         
  print(i, end="")



print()
a.execute("SELECT * from frcast WHERE country = 'India'")
b = a.fetchall()
for i in b:                            
  print(i, end="")



print()
a.execute("SELECT * from frcast WHERE season = 'Fall'")
b = a.fetchall()
for i in b:                            
  print(i, end="")



print()
a.execute("SELECT city,country,season from frcast WHERE rainfall BETWEEN 200 and 400")
b = a.fetchall()
for i in b:                                
  print(i, end="")



print()
a.execute("SELECT city,country from frcast WHERE (season = 'Fall' and temperature > 20) Order BY temperature ASC ")
b = a.fetchall()
for i in b:                             
  print(i, end="")



print()
a.execute("SELECT sum(rainfall) from frcast WHERE city = 'Cairo'")
b = a.fetchall()
for i in b:
  print(i)
print
print()
a.execute("SELECT season, sum(rainfall) from frcast group by season")
b = a.fetchall()
for i in b:                                
  print(i)



conn.close()


# # Question 9

# In[26]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print([x.upper() for x in words])
print([x.lower() for x in words])
print([len(x) for x in words])
print([[x.upper(), x.lower(), len(x)]for x in words])
print([x for x in words if len(x) >= 3])

