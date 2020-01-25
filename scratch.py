# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:07:19 2019

@author: rjsta
"""

string = "This has text."
string[0] #indexing
len(string) #length of string
string[-2] #indexing second to last char
print(string[5:12]) #substring
string[:5]
string[12:]
string2 = 2 * ('Con' + 'catenation') #concatenation twice
#String Manipulation
word = "Ford"
word = "L" + word[1:]
#Format Method: better way to concate
print("The {car} has an mpg of {0} and a tank size of {1} gal.".format(53, 8, car = "Camry"))
print("{:<10}".format("Word")) #Left allign 10 spaces
print("{:>10}".format("Word")) #Right allign 10 spaces
print("{:b}".format(12)) #Print 12 in binary

#Ternary Operator
a = 7 if 3*2 > 4 else 12
print(a)

#for-loops
for i in range(0,12,2): #i goes from 0 to 12 in increments of 2
    print(i)

text = "This is loop."
for i in range(len(text)):
    print(text[i])
    
#10x10 multiplication table
for i in range(1,11):
    for j in range(1,11):
        print("{:<3}|".format(i*j),end="") #end="" parameter prevents new line creation
    print()