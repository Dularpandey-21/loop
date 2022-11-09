# for loop 
n=int(input("enter number number"))
sum=0
for a in range(1,n+1):
    f=1    
    for b in range(1,a+1):        
        f=f*b        
    sum=sum+f   
print(sum)        


# while loop 
n=int(input("enter the number"))
sum=0
i=1
while i<=n:
    j=1
    f=1
    while j<=i:
        f=f*j
        j=j+1
    sum=sum+f
    i=i+1
print(sum)