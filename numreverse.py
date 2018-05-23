'''n1=int(input("Enter starting number:"))
n2=int(input("Enter ending number:"))

for n1 in range(n2,n1-1,-1):
       print(n1) '''
  
n3=int(input("Enter number:"))
str=''
rev=0
while n3>0:
   n3,r=divmod(n3,10)
   rev=rev*10+r
   print "rev:%d r:%d" %(rev,r)

print(rev)
   
       
