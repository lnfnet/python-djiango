#!/bin/usr/env python

items = {'number':42,
         'text':"hello world"
         }
items["func"] = abs
import math
items["mod"] = math
items["error"] = ValueError
nums = [1,2,3,4]
items["append"] = nums.append


#test

items["func"](-15)
