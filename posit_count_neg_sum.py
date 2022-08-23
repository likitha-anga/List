list=[1,2,3,4,5,6,7,8,9,-1,-3,-4,-5,-6,-7,-89]
i=0
c=0
s=0
while i<len(list):
    if list[i]>0:
        c+=1
    else:
        s=s+list[i]
    i+=1
print([c,s])
        
