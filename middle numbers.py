a=[1,3,5]
i=1
b=[]
while i<len(a)+2:
    if i not in a:
        b.append(i)
    i+=1
print(b)

list=[1,3,5,7,9]
i=1
a=[]
while i<len(list)+4:
    if i not in list:
        a.append(i)
    i+=1
print(a)
        