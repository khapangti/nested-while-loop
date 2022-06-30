i=1
k=1
while i<=4:
    col=1
    while col<=4-i:
        print(" ",end=" ")
        col=col+1
    j=1
    while j<=k:
        print("*",end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1