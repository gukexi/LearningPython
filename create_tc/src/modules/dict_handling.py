'''
Created on Jul 18, 2019

The module contains one function.
The function needs an input parameter and a return value.
The input parameter is a dictionary.
The return value is a list.
The function is to change the dictionary to the list.

@author: ekexigu
'''

def list_from_dict(new_dict):
    new_lists = []
    new_lists.append(new_dict["Measure_Points_Description"])
    new_lists.append(new_dict["Branches"])
    new_lists.append(new_dict["Continuous"])
    return new_lists