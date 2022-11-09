# while loop 
n=int(input("enter the number"))
i=1
num=0
while i<=n:
    b=int(input("enter the next number"))
    if num<=b:
        num=b
    i=i+1
print("the max number is",num)


# for loop 
# n=int(input("enter the number"))
# num=0
# for i in range(n):
#     b=int(input("enter the next number"))
#     if num<=b:
#         num=b
#     # i=i+1
# print("the max number is",num)