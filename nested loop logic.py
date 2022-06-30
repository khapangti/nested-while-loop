i=1
sum=1
while i<=4:
    j=1
    while j<=i:
        if j==1:
            print(j,end=" ")
        else:
            sum=sum+1
            print(sum*2,end=" ")
        j=j+1
    print()
    i=i+1