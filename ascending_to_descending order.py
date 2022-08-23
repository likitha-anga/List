# ascending order:
     
# list=[5,3,66,266,63,754,4,55]
# list.sort()
# print(list)
# 
# descending order:

# list=[3,43,443,66,77,646,860]
# list.sort(reverse=True)
# print(list)
# 

list=[2,0,34,5,0,0,43,2,4,56,4]
i=0
a=[]
b=[]
while i<len(list):
    if list[i]!=0:
        c=list[i]
        a.append(c)
    else:
        d=list.sort()
        b.append(d)
    i+=1
e=a+b
print(e)






