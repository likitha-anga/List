list=[1,-1,2,-2,0,3,-3,4,-4,5,-5,0,0,-6,7,-7,8,-8,9,-9,10,-10]
i=0
a=[]
b=[]
c=[]
while i<len(list):
    if list[i]>0:
        a.append(list[i])
    elif list[i]<0:
        b.append(list[i])
    else:
        c.append(list[i])
    i+=1
print(a)
print(b)
print(c)