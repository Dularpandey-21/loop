n=int(input("enter the rows number"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print() 



i=1
j=int(input("enter the number:-"))
while i<=10:
    print(i,'*',j,'=',j*i)
    i=i+1