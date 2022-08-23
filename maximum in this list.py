# list=[50,40,23,10,12,5,7,10]
# i=0
# maximum=0
# while i<len(list):
#     if list[i]>maximum:
#         maximum=list[i]
#     i=i+1
# print(maximum)

# list=[50,40,23,70,56,12,5,7,10]
# i=0
# max=list[0]
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     i=i+1
# print(max)
    
    

    
    

# list=[23,54,21,35,6,7,43,46,65]
# i=0
# max=0
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     i=i+1
# print(max)


# list = [50, 40, 23, 70, 56, 12, 5, 10, 7]
## i=0
# max=list[0]
# while i<len(list):
#     if max<list[i]:
#         max=list[i]
#         max=list[i]
#     i=i+1
# print(max)


# list = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=list[0]
# while i<len(list):
#     if max<list[i]:
#         max=list[i]
#     i=i+1
# print(max)



# list=[1,2,3,4,5]
# max=0
# i=0
# while i<len(list):
#     if max< list[i]:
#         max=list[i]
#     i=i+1
# print(max)
# n=int(input("enter the number:"))
# i=0

i=1
a=[]
while i<=10:
    n=int(input("enter number"))
    a.append(n)
    i=i+1
print(a)
max=0
min=a[0]
j=0
while j<len(a):
    if a[j]>max:
        max=a[j]
    elif a[j]<min:
        min=a[j]
    j=j+1
print("max","=",max)
print("min","=",min)

list=[2,3,4,5,6]
i=0
min=list[i]
while i<len(list):
    if min>list[i]:
        min=list[i]
    i+=1
print(min)

list=[2,3,4,5,1]
i=0
min=list[i]
while i<len(list):
    if min>list[i]:
        min=list[i] 
    i+=1
print(min)

list=[1,2,3,4,5,6,7]
i=0
max=0
while i<len(list):
  if list[i]>max:
      max=list[i]
  i+=1
print(max)