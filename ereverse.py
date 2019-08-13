n=int(input("enter the size"))
a=[]
c=[]
for i in range(n):
    b=int(input("enter"))
    a.append(b)
x=sorted(a)
if(x.count(0)==len(x)):
    print(a[0])
else:
    for i in range(len(x)-1,-1,-1):
        print(x[i])
