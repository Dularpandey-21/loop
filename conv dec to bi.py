# convert decimal to binary

i=int(input("enter the number"))
sum=0
while i>0:
    a=i%2
    sum=sum*10+a
    i=i//2
print(sum)