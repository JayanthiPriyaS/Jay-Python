num=input("Enternumber:")
i=1
s=0

for i in range(i,num):
       if(num%i==0):
           print "i:%d" %(i)
           s=s+i
           print "s:%d" %(s)
if(num==s):
   print("number is a perfect number")
else:
   print("number is not a perfect number")           



'''
factorlist=[]
   for i in range(i,num):
       if(num%i==0):
           factorlist.append(i)
   print "Length of list:%d"  %(len(factorlist))
   print "Sum of list:%d"     %(sum(factorlist))
   print "Maximum of list:%d" %(max(factorlist))
   print "Minimum of list:%d" %(min(factorlist))

if(num==(sum(factorlist))):
   print("number is a perfect number")
else:
   print("number is not a perfect number")
 '''

          
     
   
