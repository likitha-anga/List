list = [0,1,0,3,12]
i=0
a=[]
b=[]
count=0
while i<len(list):
    if list[i]==0:
        a.append(list[i])
        count+=1
    else:
        b.append(list[i])
    i+=1
c=(b+a)
print(c)
print([count])