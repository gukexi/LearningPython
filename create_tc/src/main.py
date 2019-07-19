'''
Created on Jul 19, 2019

@author: ekexigu
'''

from os import path as p
from modules import json_handling as jh
from modules import dict_handling as dh
from modules import create_tc_measure_points as ctmp

current_path = p.dirname(__file__)
json_operate = open(p.join(current_path, 'TC configuration.json'), 'r')
tc_operate = open(p.join(current_path, 'TC_Temp.txt'), 'w')

ctmp.creat_comments(dh.list_from_dict(jh.load_json_file(json_operate)), tc_operate)

json_operate.close()
tc_operate.close()