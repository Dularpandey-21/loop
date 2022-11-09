# i=1
# while i<5:
#     print("#"*i)
#     i=i+1

# i=5
# while i>=1:
#     j=5
#     while j>=1:
#         print(i,end=" ")
#         j=j-1
#     print()
#     i=i-1



i=0
while i<=5:
    j=1
    a=65
    while j<=i:
        if i%2==0:
            print(chr(a),end=' ')
            a=a+1
        else:
            print(i,end=' ')
        j=j+1
    i=i+1
    print()