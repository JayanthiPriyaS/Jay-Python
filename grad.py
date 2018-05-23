import math
sub1=float(input("Enter marks of subject1:"))
sub2=float(input("Enter marks of subject2:"))
sub3=float(input("Enter marks of subject3:"))
sub4=float(input("Enter marks of subject4:"))
sub5=float(input("Enter marks of subject5:"))        


total= sub1+sub2+sub3+sub4+sub5
avg=math.trunc(total/5)
print("avg:", avg)

#avg=int(total/5)

if(avg>=90)and(avg<=100):
    print("Grade is A+")
elif(avg>=80) and (avg<=90):
    print("Grade is A")
elif (avg>=60) and (avg<=80):
    print("Grade is B+")    
elif (avg>=45) and (avg<=60):
    print("Grade is B+")
elif(avg>=35) and (avg<=45):
    print("Grade is C")
else:
    print("Grade is fail")



'''if(avg in range(90,101)):
    print("Grade is A+")
elif(avg in range(80,91)):
    print("Grade is A")
elif(avg in range(60,81)):
    print("Grade is B+")
elif(avg in range(45,61)):
    print("Grade is B")
elif(avg in range(35,46)):
    print("Grade is C")    
else:
    print("Grade is fail")'''
