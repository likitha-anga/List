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