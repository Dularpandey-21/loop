# while loop 
n=int(input("enter the number"))
row=0
while row<=n-1:
    val=row+1
    dec=n-1
    col=0
    while col<=row:
        print(val,end=" ")
        val=val+dec
        col=col+1
    print()
    row=row+1    


# for loop         
n=int(input("enter the number of rows"))
for row in range(n):
    val=row+1
    dec=n-1
    for col in range(row+1):
        print(val,end=" ")
        val=val+dec
    print()