#!/usr/bin/env python3
#Author: Kushal Parmar
#Author ID: kparmar24 
#File Name: lab3b.py
#Date: 30th Sept, 2024

#def square(number):
#   return number ** 2
#print(square(5))
#print(square(10))
#print(square(12))
#print(sqaure(square(2)))
#print(square('2'))

#def sum_numbers(number1, number2):
#   return int(number1) + int(number2)
#print(sum_numbers(5, 10))
#print(sum_numbers(50, 100))
#print(square(sum_numbers(5, 5)))


def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # remember to make sure the function acepts 2 arguments
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
