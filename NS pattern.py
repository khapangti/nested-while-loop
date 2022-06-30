i=1
sum=0
while i<=5:
    j=1
    while j<=i:
        if j==1:
            print(j,end=" ")
        else:
            sum=sum+1
            print(sum,end=" ")
        j=j+1
    print()
    i=i+1
    