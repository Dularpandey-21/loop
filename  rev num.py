n=int(input("enter number"))
reverse=0
while n>0:  
    reverse=(reverse*10)+n%10  
    n=n//10    
print("Reverse number=",reverse)    