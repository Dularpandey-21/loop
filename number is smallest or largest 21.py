n=int(input("enter first number"))
g=n
s=n
for i in range(n):
    n=int(input("enter the next number"))
    if n>g:
        g=n
    elif n<s:
        s=n
print()
print("largest number is",g)
print("smallest number is",s)