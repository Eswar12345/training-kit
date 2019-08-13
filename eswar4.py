n=int(input("enter the size"))
a=[]
for i in range(n):
    b=input("enter")
    a.append(b)
for i in range(n):
    count=a.count(i)
    if(count==1):
        print(i)
