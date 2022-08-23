list=['m','a','d','a','m']
i=1
rev_list=[]
while i<=len(list):
    b=list[-i]
    rev_list.append(b)
    i=i+1
if rev_list==list:
    print("polindrome")
else:
    print("not pollindrome")

