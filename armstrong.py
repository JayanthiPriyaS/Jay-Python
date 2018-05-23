''' n1=int(input("Enter starting range:"))
n2=int(input("Enter ending range:")) '''

n3=int(input("Enter number:"))
n4=n3
countdigit=0
i=1
r3=1
r4=0

while n3>0:
  n3,r=divmod(n3,10)
  countdigit=countdigit+1
print"countdigit:%d" %(countdigit)
n3=n4
while n4>0:
      n4,r2=divmod(n4,10)
      n5=1
      for i in range(countdigit):
          n5=n5*r2
          print"i:%d" %(i)
          print "r2:%d" %(r2)
          print"countdigit:%d" %(countdigit)
          print "n5:%d" %(n5)
      r4=r4+n5
      print "r4:%d" %(r4)
print(r4)
if(n3==r4):
    print("num is armstrong")
else:
     print("num is not armstrong")
 
