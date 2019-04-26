'''
Created on Apr 26, 2019

@author: ekexigu
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']
if len(cars) > 0:
    print(cars)
else:
    print("The list is empty.")
    
if 'honda' not in cars:
    print("honda isn't contained in the list.")
    
age=10
if age >= 8 and age <= 18:
    print("you are a teenager.")
elif age < 8:
    print(("you are a baby."))
else:
    print("you are a adult.")