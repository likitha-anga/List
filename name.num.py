list="likitha"
i=0
while i<len(list):
    print(list[i])
    i=i+1
    # 
# list=("likitha","harsha")
# i=0
# c=[]
# while i<len(list):
#     c.append(list[i])
#     i=i+1
# print(c)
    
# list=["g","o"],["v","i"],["n","d"],["h","a"],["r","s"],["h","a"]
# output: govindharsha
# i=0
# while i<len(list):
    # j=0
    # while j<len(list[i]):
        # print(list[i][j],end="")
        # j=j+1
    # i=i+1
# 
# 

list="likitha"
i=0
c=0
while i<len(list):
    s=list[i]
    if s==list[i]:
        c=list[i]
    i=i+1
print(c)


list=[1,2,3,4,5,3,5]
i=0
c=0
b=[]
while i<len(list):
    if list[i] not in b:
        s=list[i]
        c=c+1
    i+=1
print(c)
        