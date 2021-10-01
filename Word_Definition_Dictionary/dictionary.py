#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:53:54 2021

@author: jarvis
"""

import json
from difflib import get_close_matches

data = json.load(open("/home/jarvis/Downloads/Projects/data.json"))

def translate(word):
    word = word.lower()
    if word in data: # if word in dictionary this will return it.
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(word, data.keys())[0])
        if yn in ['Y', 'y','yes','Yes','YES']:
            return data[get_close_matches(word, data.keys())[0]]
        elif yn in ['n','N','No','no','NO']:
            return "The Word Doesn't exist! Double check it!"
        else:
            return "We didn't understand! Please try again!"
    else:
        return "The Word Doesn't exist! Double check it!"

user_input = input("enter your word: ")

output = translate(user_input)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
