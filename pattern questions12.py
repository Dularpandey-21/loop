# n=int(input("enter the number of rows"))        
# for i in range(n):
#     p=5
#     for j in range(i+1):
#         print(p,end=" ")
#         p=p-1
#     print() 


n=int(input("enter the number of rows"))
i=0
while i<=n:
    j=0
    p=5
    while j<i:
        print(p,end=" ")
        j=j+1
        p=p-1
    print()
    i=i+1         