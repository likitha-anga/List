num1=int(input("enter the numbers:"))
num2=int(input("enter the numbers:"))
count=0
while num1<num2:
    if num1%10==2 or num1%10==3 or num1%10==9:
       count+=1
    num1=num1+1
print(count)

    
    
    
    
