'''
Created on Jul 18, 2019

The module contains one function.
The function needs an input parameter and a return value.
The input parameter is json file operating.
The return value is a dictionary.
The function is to load json file and return the dictionary.

@author: ekexigu
'''

from json import load as l

def load_json_file(json_operate):
    return l(json_operate)