number=30
list=[10,11,12,13,14,17,18,19]
i=0
a=[]
while i<len(list):
    b=[]
    j=0
    while j<len(list):
        if list[i]+list[j]==number and list[j]>list[i]:
            b.append(list[i])
            b.append(list[j])
            a.append(b)
        j+=1
    i+=1
print(a)
8
        
    