# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

#PRINT EXERCISES
print ('K')
print ('A')
print ('S')
print ('S')
print ('A')
print ('U')
print ('N')
print ('D')
print ('R')
print ('A')
# No variables appear in variable explorer


# print('\n'.join(map((lambda x: x), "Kassaundra")))

# OPERATION EXERCISES

print(5/2)
print(5.0/2.0)
# i get the same answer

print(7%5)
print(5%7)
# modulo is hard for me to figure out. 
# in the first example, it prints 2 because there is a remainder of 2 when you have 7 fifths
# in the second example it is easier to think of it as 0 + 5/7. 
# Thinking about it like this, the answer is 5 because everything is the remainder. 
print(9%4)
print(1%4)
# first example rephrased as 2+1/4 (or 9/4). prints one because 1 quarter remains.
# second example also prints 1. 0+1/4. 1 quarter remains

print(3**2)
print(3**3)
#exponents. 3 squared and 3 cubed shown here.

print(6/7)
print(6//7)
# the // operator divides, but rounds Down to the nearest integer even if the decimal value is >5

print(5 + 3 + 2 * 6 / 2)
# yep it does follow the order of ops 



# VARIABLE EXERCISES

letter1 = 'K'
letter2 = 'A'
letter3 = 'S'
letter5 = 'U'
letter6 = 'N'
letter7 = 'D'
letter8 = 'R'
print(letter1, letter2, letter3, letter3, letter2, letter5, letter6, letter7, letter8, letter2)
# now we have 8 vars in the variable explorer, one for each letterX

letterX = 'A'
print(letter2, letterX)
# python has no issues with this, just adds an extra variable to the explorer

letterX= 'Z'
print(letter2, letterX)
# redifining letterX does not affect letter2 in this case

letterX = letter1
print(letterX, letter1)
#yep, letterX is now redefined to hold the same value as letter1

letter1 = 'Z'
print(letterX, letter1)
# letterX is still equal to K, because i redefined letter1 after letterX was already assigned to the previous letter1 value
# if i change the original assignmnet of letter1 on line 57, then letterX will also be redeifined to that value
# variable assignment in python holds to above lines, it is sequential. hope i am making sense haha

#BOOLEAN EXERCISES

print(1+3)
print(1.0+3)
print(1/2)
# 1.0 is a float, so it will always cause the print to print with decimals
# 1 is an integer, so it will print without decimals unless necessary as shown in line 89 which prints 0.5
# differnt because they produce different outputs while the rest of the function is the same
print('1', '1.0')
print ('1'+'2') #this is not doing a math operation, just printing 1 and 2 in a sequence
print('1.0'+'2') # ditto as line 94
# '1' and '1.0' are not the same. these are strings now, not variables. They print as they are typed.

print(5, (3+2))
# they both return the same value, in that sense they are equivalent
# philosophically idk

print( 1==1.0 and 5==(2+3) and not '1'=='1.0')
print( 1==1.0 or 5==(2+3) and not '1'=='1.0')
print( 1==1.0 and 5==(2+3) and '1'!='1.0')
print( 1==1.0 and 5==(2+3) or '1'!='1.0')
print( 1==1.0 and not 5!=(2+3) or '1'!='1.0')
# 5 different iterations that all return True

# LIST EXERCISES

oddlist = [1, 3, 5, 7, 9]
# ya thats a variable now
print(oddlist)
print(len(oddlist))
# it is 5 long
print(type(oddlist))
# class of oddlist is list
intlist = []
for i in range(101) :
    intlist.append(i)
    
print(intlist)
# good list :)

# DICTIONARY EXERCISES

about_me = {
    'name': 'Kassaundra',
    'age': 22.0,
    'year of study': 4,
    'favorite foods': ['icecream', 'costco hotdog', 'sushi']
    }
print(about_me)
# type is listed in variable explorer as a dictionary
print(len(about_me))
# length is 4 because there are 4 elements

# ARRAY EXERCISES

mixnum = np.array([1, 2, 3, 4.0, 5.0, 6.0])
print(mixnum)
# looks like the array became all floats
print(type(mixnum))

mixtypes = np.array([1, 2, 3.0, 4.0, 'tiger', 'octopus'])
print(mixtypes)
# now the integers did not print as floats, but now they all have the apostrophes that make it a string

oddarray = np.arange(1,100,2)
print(oddarray)

logarray = np.logspace(1,5,16)
print(logarray)

# tried to follow the plotting part of the Sep 19 class, but spyder doesn't recognize matplotlib.pyplot










