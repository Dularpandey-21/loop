# i=1    
# while i<=5:
#     print("#"*i)
#     i=i+1



#make a program 1 to 100,number divisible by 3 print "nav",number divisible 7 gurukul ,3 and 7 divisible 3 and 7 print "navgurukul
# i=1
# while i<=100:
#     if i%3==0:
#         print(i,"nav")
#     elif i%7==0:
#         print(i,"gurukul")
#     elif i%3 and i%7==0:
#         print(i,"navgurukul")
#     i=i+1



#input 10 numbers,prints the sum of all those numbers
# i=1
# sum=0
# while i<=10:
#     user=int(input("enter the number"))
#     sum=sum+user
#     i=i+1
# print(sum)

#print number 11 to 101 ,counter from 15




#print loop 20 to 100 divisible by 2 and riminder 0
# i=20
# while i<=200:
#     if i%2==0:
#         print(i)
#     i=i+1

# # print loop 10 to 100 divisible by 7
# i=10
# while i<=100:
#     if i%7==0:
#         print(i)
#     i=i+1

# #write a program that calculate the "total" from  12 to 421
# i=1
# sum=0
# while i<=400:
#     sum=sum+i
#     print(sum)
#     i=i+1

#calculates the sum of those numbers from 30 to 420 which are multiple of 8
# i=30
# sum=0
# while i<=420:
#     if i%8==0:
#         sum=sum+i
#         print(sum)
#     i=i+1

#take inputof weight of 11 people and their print average meraki ,question 5 
i=1
sum=0
while i<=11:
    weight=int(input("enter the weight"))
    i=i+1
    sum=weight+sum
print(sum/11)
if (sum/11)%5==0:
    print('divisible by 5')
else:
    print("not divisible by 5")
    
