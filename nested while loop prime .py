n=int(input("enter number"))
a=1
while a<=n:
    i=2
    while i<=a//2:
        if a%i==0:
            break
        i=i+1
    else:
        print("prime",a)
    a=a+1