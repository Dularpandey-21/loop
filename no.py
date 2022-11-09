# for loop 
n=int(input("enter the number of rows"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print() 


# # while loop   
# n=int(input("enter the number of rows"))
# num=1
# row=1
# while row<=n:
#     col=1
#     while col<=row:
#         print(num,end=" ")
#         col=col+1
#         num=num+1
#     print()
#     row=row+1
