#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:39:59 2018

@author: ak
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from math import factorial


# Homework I

# PART I: Writing Functions. 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

#1 Write a function that tests if a vector x is longer than a vector y.
  
    # x and y are two vectors 
    
def test_length(x,y):
    if len(x) > len(y):
        print('x is longer than y')
    else: 
        print('y is longer than x')

    # Test the function test_length()
    
x = np.array([2, 3, 1, 5])
y = np.array([1, 2, 15, 17, 18, 20])    

test_length(x,y)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

#2 Write a function that tests if a vector x has more elements that are 
#  greater than 5 than a vector y.

    # x and y are two vectors 
    
def more_than5(x,y):
    if len(x[x>5]) > len(y[y>5]):
        print('x has more elements that are greater than 5 than y')
    else:
        print('y has more elements that are greater than 5 than x')
            
    # Test the function more_than5()

x = np.array([2, 3, 1, 5])
y = np.array([1, 2, 15, 17, 18, 20])    

more_than5(x,y)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3 Write a function with three arguments (x,y, and c, where c is a scalar) that 
#  tests if a vector x has more elements that are smaller than c than vector y.

def more_thanC(x,y,c):
    if len(x[x<c]) > len(y[y<c]):
        print('x has more elements smaller than c than y')
    else:
        print('y has more elements smaller than c than x')

    # Test the function more_than5()

x = np.array([2, 3, 1, 5])
y = np.array([1, 2, 15, 17, 18, 20])    
c = 4

more_thanC(x,y,c)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4 Suppose you have two vectors, x and y, each with 3 distinct elements.  Write 
#  a function that returns the number of elements that x and y have in common 
#  (e.g.  if the vectorsare c(1,2,3) and c(3,6,2), it should return 2).

def no_common_elements(x,y):
    z = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                z += 1
            else:
                z += 0
    return z

    # Test the function common_elements()
    
x = np.array([1, 2, 3])
y = np.array([3, 6, 2])

no_common_elements(x,y)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#5 A bit more tricky: Suppose you have two vectors, x and y, each with 3 
#  distinct elements.Write a function that returns the elements that x and y 
#  have in common (e.g.  if thevectors are c(1,2,3) and c(3,6,2), it should 
#  return 2 and 3).

def common_elements(x,y):
    z = np.array([])
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                z = x[i]
    return(z)

    # Test the function common_elements()
    
x = np.array([1, 2, 3])
y = np.array([3, 6, 2])

common_elements(x,y)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# PART II: Writing Advanced Functions using Loops

#1 Euler’s number. Write a loop that approximates this number. 

def sumE(n):
    sum = 0 
    for i in range(n):
        sum += 1/factorial(i)
    return(sum)

    # Test the function sumE()
    
n = 100

sumE(n)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#2 Using your code from (1), find the number c from which on the approximation

def findC(n):
    sum = 0
    for i in range(n):
        sum += 1/factorial(i)
        if sum == 2.71828:
            stop
    return(i)

    # Test the function findC()
    
findC(100)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3 Suppose you have 2 equally long vectors a and b.  Write a function that 
#  returns the index of the first time both are equal (E.g.  if a<−c(1,4,8,12) 
#  and b<−c(5,2,8,10)it should return 3).  If both vectors are not equal for 
#  any position, it should return 0.

def returnIndex(x,y):
    for i in range(len(x)):
        if x[i] == y[i]:
            print('The index is', i)        
            
    # Test the function returnIndex()
    # Remember that index in Python starts from 0. 

x = np.array([1, 4, 7, 12])
y = np.array([5, 2, 7, 10])
ga
returnIndex(x,y)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4 Write a function that takes n as input and creates the following matrix

def matrixN(n):
    m = np.zeros(shape = (n,n))
    for i in range(n):
        m[i,i] = i**2
    return(m)
        
    # Test the function matrixN()

n = 10

matrixN(n)
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






# Homework II

# Part II: Writing Functions and Loops. 

#1 Use for-loops to compute:

sum = 0 
for i in range(1,10):
    for j in range(1,10):
        sum += (i - j) ** 2
print(sum)

#2 Now, compute the same expression but use while-loops instead.

n = 10
sum = 0
i = 1
while i < n:
    j = 1
    while j < n:
        sum += (i - j) ** 2
print(sum)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3 Use loops to compute. 

n = 10
sum = 0
for i in range(n):
    for j in range(n):
        if i > j: 
            sum += (i - j) ** 2
print(sum)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4 The Gini Coefficient is one of the most common measures of inequality used 
#  in economics.  Write a function that computes the Gini-Coefficient for any 
#  vector x.

def Ginny(x):
    num = 0
    den = 0
    for i in range(len(x)):
        for j in range(len(x)):
            num += abs(x[i] - x[j])
            den += 2*x[i]
    return(num/den)

    # Test the function Ginny()

x = np.array([1,2,10,17,200, 1000])

Ginny(x)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++











