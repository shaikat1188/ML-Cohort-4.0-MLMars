# Write a program that: 
# Creates a tuple with the names of 5 cities. 
# Prints the third city in the tuple. 
# Converts the tuple into a list, adds a new city, and converts it back to a tuple. 
# Prints the modified tuple.

a=input('Enter 1st City: ')
b=input('Enter 2nd City: ')
c=input('Enter 3rd City: ')
d=input('Enter 4th City: ')
e=input('Enter 5th City: ')

mytuple=(a,b,c,d,e)

print(f'The 3rd City: {mytuple[2]}')

mylist=list(mytuple)

x=input('Enter New city: ')
mylist.append(x)

newtuple=tuple(mylist)

print(f'Modified Tuple: {newtuple}')