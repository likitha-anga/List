list1 = ["Shogun","Tapioca Express","Burger"]
list2 = ["KFC","Shogun","Burger King"]
i=0
a=[]
while i<len(list2):
    if list1[i] in list2:
        a.append(list1[i])
        break
    i+=1
print(a)