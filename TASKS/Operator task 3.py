a=7 # 7=111
b=4 # 4=100
c= a | b
d=a & b
e= a^b
print(c,d,e)

'''
a ^ b explanation
	Sets each bit to 1 if only one of two bits is 1
    so for 111 and 100 placing 1 to the place where only one of two bits
    is 0, we get 011 for which we get 1+2=3 
'''

