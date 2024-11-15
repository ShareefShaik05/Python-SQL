#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 7 12:00:46 2022

@author: Shareef Shaik
"""

#####################################################
##### Practice Problem 3.1, Page 57 #################
#####################################################

# Implement a program that requests the current temperature in degrees Fahrenheit
# from the user and prints the temperature in degrees Celsius using the formula
# celsius= (5/9) * (fahrenheit -  32)

fahrenheit = eval(input("Enter the temp in degrees F: "))
celsius = 5/9 * (fahrenheit - 32)
print ("The temp in degrees celsius is", celsius)

#####################################################
##### Practice Problem 3.2, Page 60 #################
#####################################################

# Translate these conditional statements into Python if statements:
age= 75
# (a) If age is greater 62, print 'You can get your pension benefits'.
if age > 62 :
    print ("You can get your pension benefits" )
# (b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], 
# print 'One of the top 5 baseball players, ever!'. list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
name = "Ruth"
if name in ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']:
    print ("One of the top 5 baseball players, ever!")
# (c) If hits is greater than 10 and shield is 0, print 'You are dead...'.
hits = 67
shield = 0
if hits > 10 and shield == 0:
    print ("You are dead...")
# (d) If atleast one of the Boolean variables north, south, east, and west is True , print
# 'I can escape.'.

north, south, west, east = True, False, True, False
if north == True or south == False or east == True or west == False:
    print ("I can escape.")
# or   
north, south, west, east = 1,0,0,0
if north or south or east or west:
    print ("I can escape.")



#####################################################
##### Practice Problem 3.3, Page 62 #################
#####################################################

# Translate these into Python if/else statements:
# (a) If year is divisible by 4, print  Could be a leap year. ; otherwise print  Definitely not
# a leap year. 
year= eval(input( "Enter the year: "))
if (year % 4 == 0):
    print ("Could be a leap year")
else:
    print ("Definitely not a leap year")

# (b) If list ticket is equal to list lottery, print  You won! ; else print  Better luck next time... 

ticket = [1,3,4,5]
lottery= [1,3,4,5]

if ticket == lottery:
    print ("You won!")
else:
    print("Better luck next time...")

#####################################################
##### Practice Problem 3.4, Page 62 #################
#####################################################

# Implement a program that starts by asking the user to enter a login id (i.e., a string).
# The program then checks whether the id entered by the user is in the 
# list ['joe', 'sue', 'hani', 'sophie'] of valid users. 
# Depending on the outcome, an appropriate message should be printed. 
# Regardless of the outcome, your function should print 'Done.' before terminating. 
name= ['joe', 'sue', 'hani', 'sophie']
login1= "joe"
login2= "john"
if login1 in [name]:
    print ("You are in")
else:
    print ("User unknown")
print ("Done!")

#####################################################
##### Practice Problem 3.5, Page 65 #################
#####################################################

# Implement a program that requests from the user a list of words (i.e., strings) and 
# then prints on the screen, one per line, all four-letter strings in the list.
# >>>
# Enter word list: ['stop', 'desktop', 'top', 'post'] stop
# post

word= eval(input("Enter word list: "))
for value in word:
    if len(value) == 4:
        print (value)

#bonus to print vowels:

name= (input("Enter your name: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for character in name:
    if character in vowels:
        print(character)

#####################################################
##### Practice Problem 3.6, Page 66 #################
#####################################################

# Write the for loop that will print these sequences of numbers, one per line, in the interactive shell.
# (a) Integers from 0 to 9 (i.e.,0,1,2,3,4,5,6,7,8,9) 
for i in range(10):
    print(i)
# (b) Integers from 0 to 1 (i.e., 0, 1)
for i in range(2):
    print(i)

#####################################################
##### Practice Problem 3.7, Page 67 #################
#####################################################

# Write the for loop that will print the following sequences of numbers, one per line.
# (a) Integers from 3 up to and including 12
for i in range(3,13):
    print(i)
# (b) Integers from 0 up to but not including 9, but with a step of 2 instead of 
# the default of 1 (i.e., 0, 2, 4, 6, 8)
for i in range(0,9,2):
    print(i)
# (c) Integers from 0 up to but not including 24 with a step of 3
for i in range(0,24,3):
    print(i)
# (d) Integers from 3 up to but not including 12 with a step of 5
for i in range(3,12,5):
    print(i)


#To call the function you type the function name with ()
# You can globally call import math first before starting anything else so it applies for all instead of under each question.

#####################################################
##### Practice Problem 3.8, Page 68 #################
#####################################################

# 3.8. Define, directly in the interactive shell, function perimeter() that takes, as input, the ra- dius of a circle (a nonnegative number) and returns the perimeter of the circle. A sample usage is:
#    >>> perimeter(1)
#    6.283185307179586
#    >>> perimeter (2)
#    12.566370614359172
# Remember that you will need the value of ? (defined in module math) to compute the perimeter.

r = eval(input("Enter the radius of the circle r: "))
def perimeter(r):
    import math
    p= 2 * math.pi * r
    return p
print (perimeter(r))

#####################################################
##### Practice Problem 3.9, Page 69 #################
#####################################################

# 3.9. Implement function average() that takes two numbers as input and returns the average of the numbers. You should write your implementation in a module you will name average.py. A sample usage is:
#    >>> average(1,3)
#    2.0
#    >>> average(2, 3.5)
#    2.75

num1= eval(input("Enter the first number: "))
num2= eval(input("Enter the second number: "))
def average(num1,num2):
    avg = (num1+num2)/2
    return avg
print (average(num1,num2))

#####################################################
##### Practice Problem 3.10, Page 69 #################
#####################################################

# 3.10. Implement function noVowel() that takes a string s as input and returns True if no char- acter in s is a vowel, and False otherwise (i.e., some character in s is a vowel).
# >>> noVowel('crypt') True
# >>> noVowel('cwm') True
# >>> noVowel('car') False

def noVowel(s):
    vowels = "aeiouAEIOU"
    for letter in s:
        if letter in vowels:
            return False
    return True

#Another Way

# s = eval(input("Enter the string s: "))
# def noVowel(s):
#     vowels = "aeiouAEIOU"
#     for char in s:
#         if char in vowels:
#             return False
#     return True
# print (noVowel(s))

#####################################################
##### Practice Problem 3.11, Page 69 #################
#####################################################

# 3.11. Implement function allEven() that takes a list of integers and returns True if all integers in the list are even, and False otherwise.
#    >>> allEven([8, 0, -2, 4, -6, 10])
#    True
#    >>> allEven([8, 0, -1, 4, -6, 10])
#    False

def allEven(list):
    for num in list:
        if num % 2 != 0:
            return False
    return True


#####################################################
##### Practice Problem 3.12, Page 71 #################
#####################################################

# 3.12. Write function negatives() that takes a list as input and prints, one per line, the negative values in the list. The function should not return anything.
#    >>> negatives([4, 0, -1, -3, 6, -9])
#    -1
#    -3
#    -9

def negatives(lst_num):
    for num in lst_num:
        if num < 0:
            print (num)

#####################################################
##### Practice Problem 3.13, Page 73 #################
#####################################################

# 3.13. Add appropriate docstrings to functions average() and negatives() from Practice Prob- lems 3.9 and 3.12. Check your work using the help() documentation tool. You should get, for example:
#    >>> help(average)
#    Help on function average in module __main__:
#    average(x, y)
#        returns average of x and y

help(average)
average (1,3)

#####################################################
##### Practice Problem 3.15, Page 78 #################
#####################################################

# Suppose a nonempty list team has been assigned. Write a Python statement or statements that swap the first and last value of the list. So, if the original list is:
# >>> team = ['Ava', 'Eleanor', 'Clare', 'Sarah'] then the resulting list should be:
# >>> team
# ['Sarah', 'Eleanor', 'Clare', 'Ava']

team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
team[0],team[-1]=team[-1],team[0]
print (team)

#####################################################
##### Practice Problem 3.16, Page 81 #################
#####################################################

# Implement function swapFL() that takes a list as input and swaps the first and last ele- ments of the list. You may assume the list will be nonempty. The function should not return anything.
# >>> ingredients = ['flour', 'sugar', 'butter', 'apples'] >>> swapFL(ingredients)
# >>> ingredients
# ['apples', 'sugar', 'butter', 'flour']

def swapFL(lst_swap):
    if len(lst_swap) > 1:
        lst_swap[0],lst_swap[-1]=lst_swap[-1],lst_swap[0]
        #print (lst_swap)







