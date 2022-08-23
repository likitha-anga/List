a=9119
n=str(a)
b=""
i=0
while i<len(n):
    b+=n[i]+","
    c=b[0:7]
    i+=1
print("[",c,"]")