n=int(input("enter the number"))
i=1
while i<=n:
    j=2
    while j<=i+1:
        if i%j==0:
            if i==j:
                print("Prime number=",i)
            break
        j=j+1
    i=i+1