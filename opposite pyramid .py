i=1
while i<=5:
    col=1
    while col<=i:
        print("",end=" ")
    col=col+1
    j=2
    while j<=5-i:
        print("*",end=" ")
        j=j+1
    k=5
    while k>i:
        print("*",end=" ")
        k=k-1
    print()
    i=i+1