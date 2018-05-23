string1=input("Enter string:")


arr1=(string1)
arr1=arr1.lower()
arr2=arr1[::-1]
arr2=arr2.lower()


if(arr1==arr2):
   print "String is palindrome"
else:
    print "String is not palindrome"

'''if(arr1.casefold()==arr2.casefold()):
   print "String is palindrome"
else:
    print "String is not palindrome"'''
