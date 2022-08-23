# list=[1,2,3,4,4,5,6,7,5,4,6,7,5]
# i=0
# count=0
# for i in list:
    # count=count+1
    # i=i+1
# print(count)
# 


list=[1,2,3,4,5]
i=0
c=0
while i<len(list):
    c+=1
    i+=1
print(c)  

list=[1,0,2,0,3,4,0,7,6]
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
c=b+a
print(c)
print([count])

list=[43,65,48,7665,44,3232,6,5]
i=0
count=0
while i<len(list):
    count+=1
    i+=1
print(count)