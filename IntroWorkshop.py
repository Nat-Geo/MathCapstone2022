# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:44:18 2022

@author: Nathaniel Gunter

Python Coding Introduction Workshop
"""

print(7*3)

#Comment like this

x = 6 * 7  + 12
print(x)

# Python Peculiarities

## Storing Variables

age = 23

first_name = 'Nat'

print(first_name, 'is', age, 'years old.')

#Define variables before calling (DOH)

age = age + 3;
print(age)


# What is an index?

atom_name = 'helium'

print(atom_name, atom_name[0:3])

#ranges do not include the last value


# Basic Functions

## len => length of an object
print(len(atom_name))

theAnswer = 42

answer = float(theAnswer)

print(type(theAnswer))
print(type(answer))

#direct concatination
print('four'+'five')

res = print('ex')
print(res)

#Common use functions
## max, min, round
print(
max(1,2,3),
min(1,2,3),
round(3.14),
round(3.14, 1),
max('abba')
)

help(round)
def helloworld(input):
    print(input)
    return(input)

result = helloworld(x)
print(result)

# Collabroative document: http://tiny.cc/nevpuz