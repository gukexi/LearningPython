'''
Created on Apr 28, 2019

@author: ekexigu
'''

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue
    print(current_number)

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
    message = input(promt)
    
    if message != 'quit':
        print(message)
    else:
        print("\nThe end.")
    
message = ""    
while True:
    message = input(promt)
    if message == 'quit':
        print("\nThe end.")
        break
    else:
        print(message)