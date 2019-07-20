'''
Created on Jul 19, 2019

This is the main function.

@author: ekexigu
'''

from os import path as p
from modules import json_handling as jh
from modules import dict_handling as dh
from modules import create_tc_measure_points as ctmp

current_path = p.dirname(__file__)                                                  #Get the current function path.
json_operate = open(p.join(current_path, 'TC_Configuration.json'), 'r')             #Get the current json file full name and open it in 'read' mode.
tc_operate = open(p.join(current_path, 'TC_Temp.txt'), 'w')                         #Get the current txt file full name and open it in 'write mode'.

ctmp.creat_comments(dh.list_from_dict(jh.load_json_file(json_operate)), tc_operate) #Use the functions in these modules to write the comments into txt file according to json file.

json_operate.close()                                                                #End operating json file.
tc_operate.close()                                                                  #End operating txt file.