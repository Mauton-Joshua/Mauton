# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:57:20 2023

@author: AYOOLUWA-MAUTON
"""

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
 "+": add,
 "-": sub,
 "*": mul,
 "/": div,
}
def calculator():
    n1 = int(input("What is the first number?: "))
    
    for symbols in operations:
        print(symbols)
    
    should_continue = True
    while should_continue:
     operation_symbol = input("Please pick an operation: \n")
     n2 = int(input("What is the next number?: "))
     cal_function = operations[operation_symbol]
     answer = cal_function(n1, n2)
     print(f"{n1} {operation_symbol} {n2} = {answer}")
    
     if input("Type 'y' to continue with {answer} or 'n' to end calculating:") == "y":
       n1 = answer
     else:
       should_continue = False
       calculator()