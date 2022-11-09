n=int(input("enter number to check for armstrong"))
sum=0
orig=n
while n>0:
    sum=sum+(n%10)
    n=n//10
if orig==sum:    
    print("number is armstrong")
else:   
    print("number is not armstrong") 