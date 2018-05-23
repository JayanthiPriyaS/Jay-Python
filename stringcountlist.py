string=input("Enter string:")

n=len(string)
print "Length of the string:%d" %(n)

smallcount=0
uppercount=0
spacecount=0
numericcount=0
specialcount=0

for i in range(n):
    if(string[i].islower()):
       smallcount=smallcount+1
    elif(string[i].isupper()):
       uppercount=uppercount+1
    elif(string[i].isspace()):
       spacecount=spacecount+1
    else:
       specialcount=specialcount+1

       
print "smallcount:%d" %(smallcount)
print "uppercount:%d" %(uppercount)
print "spacecount:%d" %(spacecount)
print "specialcount:%d" %(specialcount)


