#Srikanth kulkarni
#Roll.no :5
#Division : L1
def sum(a,b):
	return a+b
def sub(a,b):
	return a-b
def multi(a,b):
	return a*b
def divi(a,b):
	return a/b
print("selection of choice")
print("1.add")
print("2.sub")
print("3.multiplication")
print("4.division")
choice=int(input("enter a choice"))
a=int(input("enter a number"))
b=int(input("enter other number "))
if(choice==1):
	print("sum of a+b:",sum(a,b))
elif(choice==2):
	print("subtraction of a-b:",sub(a,b))
elif(choice==3):
	print("multiplication of a*b:", multi(a,b))
elif(choice==4):
	print("division of a/b:",divi(a,b))
else:
	print("invalid choice")
