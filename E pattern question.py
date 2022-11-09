# i=0
# while i<=10:
#     j=0
#     while j<=6:
#         if j==0 or i==0 or i==5 or i==10 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     print()
#     i=i+1



for i in range(7):
    for j in range(5):
        if j==3 or i==0 or i==6:
            print("*",end="  ")
        else:
            print(end="  ")
    print()
print()
for i in range(6):
    for j in range(6):
        if (j==0 and i!=5) or (j==5 and i!=5) or i==5 and j!=0 and j!=5:
            print("*",end=" ")
        else:
            print(end="  ")
    print()