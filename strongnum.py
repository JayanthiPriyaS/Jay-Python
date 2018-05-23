num=int(input("Enternumber:"))
n1=num
i=1
r2=0

while n1>0:
      n1,r=divmod(n1,10)
      print "n1:%d" %(n1)
      print "r:%d"  %(r)
      f=1
      i=1
      for i in range(i,r+1):
             print "i:%d" %(i)
             print "r:%d" %(r)
             f= f*i
      print "f:%d" %(f)
      r2=r2+f     
print "r2:%d" %r2
if(r2==num):
    print("number is a strongnumber")
else:
    print("number is not a strongnumber")

