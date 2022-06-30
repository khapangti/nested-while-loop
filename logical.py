i=1
while i<=4:
    j=1
    while j<=4:
        if i==1 or j==1 or j==4 or i==3 or i==j*2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1