'''
Created on Jul 18, 2019

The module contains one function.
The function needs two input parameters.
The first input parameter is a list.
The second input parameter is txt file operating.
The function is to handling the list and save the comments to txt file.

@author: ekexigu
'''

from re import sub as s

def creat_comments(current_list, tc_operate):
    description_list = []
    for current_comment in current_list[0]:
        description_list.append(current_comment.replace("\'", "\""))
    
    branches = current_list[1]
    continuous = current_list[2]
    
    tc_comments = ""
    
    if continuous:
        for description in description_list:
            for branch in range(branches):
                comment = s("{%02d}", "%02d" % branch, s("{%d}", "%d" % branch, description))
                comment += "\n"
                tc_comments += comment
    else:
        for branch in range(branches):
            for description in description_list:
                comment = s("{%02d}", "%02d" % branch, s("{%d}", "%d" % branch, description))
                comment += "\n"
                tc_comments += comment
    
    tc_operate.write(tc_comments.strip())