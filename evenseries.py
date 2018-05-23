n=int(input("Enter the number:"))
i=2

if(n<=0):
    print("Enter a valid range") 
elif(n%2==0):
    n=n
else:
    n=n-1
    

'''for i in range(i,n+2,2):
       print i '''

while(i<n+2):
      print i
      i=i+2
