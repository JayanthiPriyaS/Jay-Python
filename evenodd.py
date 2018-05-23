num=int(input("Enter number:"))

a,b=divmod(num,2)
if(b==0):
    print(num, 'is even number')
else:
    print(num, "is oddnumber")
    
