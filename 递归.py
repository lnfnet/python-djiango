#!/usr/bin/python3

def factorial(num):
    if(num==0):
        return 1
    else:
        return num*factorial(num-1)

result =factorial(12)
print('the factorial result is:',result)
