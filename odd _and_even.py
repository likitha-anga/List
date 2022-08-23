# list=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print(list[i])
#     i=i+1

#  list=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(list):
#     if list[i]%2!=0:
#         print(list[i])
#     i=i+1

# list=[1,2,3,4,5,6,78,9]
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print(list[i])
#     i=i+1

list=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
while i<len(list):
    if list[i]%2!=0:
        b=list[i]
        a.append(b)
    i+=1
print(a)
