n=int(input("enter the size"))
a=[]
c=[]
for i in range(n):
    b=int(input("enter"))
    a.append(b)
print(a)
for i in range(len(a)-1,-1,-1):
    c.append(a[i])
print(c)
