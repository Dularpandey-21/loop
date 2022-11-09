n=int(input("enter the number of term"))
s=0
sum1=0
print("series are",end=" ")
for i in range(n):
    s=s*10+2
    print(s,end=" ")
    sum1=sum1+s
print()
print("series sum=",sum1)