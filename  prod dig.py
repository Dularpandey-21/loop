n=int(input("enter number"))
product=1
while n>0:    
    product=product*(n%10)    
    n=n//10    
print("product of digits=",product)



# dry run
# n=56 | product=1 | while n>0: | product=product*(n%10) | n=n//10  | print("Product of digits=",product) 
# n=56 | product=1 | while 56>0 | product=1*(56%10)=6    |n=56//10=5|                                     
#                  |       5>0  | product=6*(5%10)=30    |n=5//10=0 | o/p=>                               
#                  |       0>0  |         *              |   *      | Product of digits=30 
