""" https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

Approach:
    * Note that we can use module to determine if a number is a multiple of another number.
    ex. n % m == 0 means that n is a multiple of m 
    * Using this we can check and see if a given value is a multiple of 3 or 5
    * If either condition is met then we can add the value to the total
    * With the conditions we should check right away to see if the number is negative
      if this is the case then return 0 right away before going through any additional logic
"""
def is_multiple(n, m):
    return n % m == 0

def solution(number):
    if number <= 0:
        return 0
    n = 0
    for i in range(1, number):
        if is_multiple(i, 3) or is_multiple(i, 5):
            n += i
    return n

   
    
    