#!/usr/bin/python3
import json
import os

username=input("what is your name?")


with open('pi_digits.txt','w') as file_object:
    json.dump(username,file_object)
    print(username)
    file_object.close()

with open('pi_digits.txt','r') as rfile_object:
    username=json.load(rfile_object)
    print(username)
    rfile_object.close()
