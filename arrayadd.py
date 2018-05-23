n1=input("enter limit of Array1:")
n2=input("enter limit of Array2:")
arr1=[]
arr2=[]
arr3=[]


for i in range(n1):
    arr1.append(input("Enter value of Array1:"))
for j in range(n2):
    arr2.append(input("Enter value of Array2:"))
print"Length of Array1:%d" %(len(arr1))
print"Length of Array2:%d" %(len(arr2))

arr3=[sum(n) for n in zip(arr1,arr2)]

print(arr3)
    
'''if (n1>=n2):
    n1=n1
else:
    n1=n2 

print "n1:%d" %(n1)
print "n2:%d" %(n2)
print(arr1)
print(arr2)
for i in range(n1):

        print "arr1[i]:%d" %(arr1[i])
        print "arr2[j]:%d" %(arr2[j])
        n3=(arr1[i]+arr2[j])
        print "n3:%d" %(n3)
        arr3.append((arr1[i]+arr2[i]))
print(arr3) '''
