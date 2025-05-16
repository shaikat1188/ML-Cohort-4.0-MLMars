# Write a program that: Creates a list of 5 numbers. Adds a new number to the list. Removes the second number from the list. Prints the sum of all numbers in the list.

a=int(input('Enter the First Number: '))
b=int(input('Enter the second Number: '))
c=int(input('Enter the third Number: '))
d=int(input('Enter the fourth Number: '))
e=int(input('Enter the fifth Number: '))

mylist=[a,b,c,d,e]

print(f'Your List: {mylist}')
x=int(input('Add a new number: '))

mylist.append(x)
mylist.remove(b)


print(f'Your New List: {mylist}')
print(f'The sum of the new list: {sum(mylist)}')