import math

n=int(input("Enter the number:"))

count=0

while(n>0):
     n,r=divmod(n,10)
     print(n,":n")
     count=count+1


print(count)
 
