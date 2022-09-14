l="level"
list1=list(l)
i=0
b=[]
e=[]
count=0
while i<len(list1):
    count=list1.count(list1[i])
    c=list1[i],count
    if list(c) not in b:
        if count>1:
            b.append(list(c))    
    i+=1
print(b)
g=[]
i=0
h=(b[0][1])
g.append(h)
h=(b[1][1])
g.append(h)
j=g[i]+g[i+1]
print(j)


