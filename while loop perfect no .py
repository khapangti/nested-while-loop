n=int(input("enter number"))
i=1
sum=0
while i<=n//2:
    if n%i==0:
        sum=sum+i
        i=i+1
if sum==n:
    print("perfect number")
else:
    print("not perfect number")