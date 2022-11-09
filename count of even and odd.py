n=int(input("enter the number"))
i=1
count=0
while i<=n:
    if i%2==0:
        print("even number =",i)
        count=count+1
    else:
        print("odd numner =",i)
        coun=count+1
    i=i+1
print("your count even number =",count)
print("your count odd number =",coun)