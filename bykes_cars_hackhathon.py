# n1=int(input("enter the bike:"))
# n2=int(input("enter the car:"))
# if n1>0:
    # a=n1*2
    # print("num of tyres of a bike",n1*2)
# if n2>0:
    # b=n2*4
    # print("num of tyres of a car",b)
# 
    # 
     
     
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i=0
a=[]
c=20
while i<len(list):
    if list[i]%5==0:
        a.append(c)
    else:
        a.append(list[i])
    i+=1
print(a)

bike=int(input("enter the number:"))
car=int(input("enter the number:"))
if car>0:
    print(car*4)
if bike>0:
    print(bike*2)

    
        
    