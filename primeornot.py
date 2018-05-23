num=int(input("Enter number:"))

i=2

for i in range (i, num):
     if(num%i==0):
        print "number is not prime"
        print "%d is divisible by %d" %(num,i)
        break
print("number is prime")
      
        

