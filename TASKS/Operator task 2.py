a=input('Enter CGPA of friend A= ')
b=input('Enter CGPA of friend B= ')
c=input('Enter CGPA of friend C= ')

x= float(a)
y=float(b)
z=float(c)
sum= (x+y+z)/3

if a<b and a<c:
    print('Friend A has lowest CGPA')
elif b<a and b<c:
    print('Friend B has lowest CGPA')
else: print ('Friend C has lowest CGPA')

print(f'Average CGPA is {sum}')
