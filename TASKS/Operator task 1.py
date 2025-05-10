x=input("Enter number x: ")
y=input("Enter number y: ")
z=input("Enter number z: ")
if x>y and x>z:
    print("x is largest")
elif y>x and y>z:
    print("y is largest")
elif z>x and z>y:
    print("z is largest")
elif x==y and x>z:
    print("x and y are largest")
elif y==z and y>x:
    print("y and z are largest")
elif z==x and x>y: 
    print('z and x are largest')
else: print ('x, y and z are same')
