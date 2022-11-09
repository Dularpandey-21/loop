# 1**2 + 9**2 = 82

# 8**2 + 2**2 = 68

# 6**2 + 8**2 = 100

# 1**2 + 0**2 + 0**2 = 1

n=int(input("enter the number"))
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
        print("sum",sum)
    x=sum
if sum==1:
    print(n,"is a happy number")
else:
    print(n,"is a not happy number")