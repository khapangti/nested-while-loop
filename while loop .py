n=input("enter name")
a=("a","e","i","o","u")
i=0
while i<len(n):
    if n[i] in a:
        print(n[i])
    i=i+1
b=0
while b<len(n):
    if n[b] not in a:
        print(n[b])
    b=b+1