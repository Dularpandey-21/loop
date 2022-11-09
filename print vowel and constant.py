a=input("enter the name")
count=0
c=0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
    elif i in "BCDFGHJKLMNPQRSTVWXYZ  bcdfghjklmnpqrstvwxyz":
        c=c+1
print("vowel in a=",count)
print("constant in a=",c)