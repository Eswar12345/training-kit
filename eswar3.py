n=int(input("Enter the size"))
a=[]
c=[]
for i in range(n):
    b=input("enter")
    a.append(b)
print(a)
for i in range(len(a)):
    if(a[i]==i):
        c.append(i)
if(len(c)==0):
    print(-1)
else:
    print(c)
