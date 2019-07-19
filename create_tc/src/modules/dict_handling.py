'''
Created on Jul 18, 2019

@author: ekexigu
'''

def list_from_dict(new_dict):
    new_lists = []
    new_lists.append(new_dict["Measure_Points_Description"])
    new_lists.append(new_dict["Branches"])
    new_lists.append(new_dict["Continuous"])
    return new_lists