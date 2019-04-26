'''
Created on Apr 25, 2019

@author: ekexigu
'''

# string processing
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("\n\tPython\nC\n\tJava")

favorite_language = " Python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# list processing
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[2])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[0].title())

bicycles[0] = 'bmw'
print(bicycles)

bicycles.append('trek')
print(bicycles)

del bicycles[2]
bicycles.insert(3, 'redline')
print(bicycles)

print(bicycles.pop(1))
bicycles.remove('bmw')
print(bicycles)

bicycles.reverse()
print(bicycles)

bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)

print(sorted(bicycles))
print(bicycles)

print(len(bicycles))

for bicycle in bicycles:
    print(bicycle)
    
numbers = list(range(1,6))
print(numbers)

squares = [value**2 for value in range(1,11)]
print(squares)
print(squares[1:4])

# tuple processing
dimensions = (200, 50)
print(dimensions)

dimensions = (250, 100)
print(dimensions)