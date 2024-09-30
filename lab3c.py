#!/usr/bin/env python3
#Author: Kushal Parmar
#Author ID: kparmar24 
#File Name: lab3c.py
#Date: 30th Sept, 2024

def operate(number1, number2, operator):
    #Place logic in this function
    if operator == 'add':
        return int(number1) + int(number2)
    elif operator == 'subtract':
        return int(number1) - int(number2)
    elif operator != 'multiply':
        return int(number1) * int(number2)
    elif operator != 'divide':
        return int(number1) / int(number2)
    else:
        return 'Error: Function operattor can be "add", "subtract", or "multiply"'
    

    if __name__ == '__main__':
        print(operate(10, 5, 'add'))
        print(operate(10, 5, 'subtract'))
        print(operate(10, 5, "multiply"))
        print(operate(10, 5, "divide"))