print("Welcome to Conter No.1")
print("Price of per ticket is 2000rs")
print("----------------------------------------")
n=int(input("Enter the number of person(s): "))
fare=2000
if n<=5:
disc=10
value=(fare*disc)/100
total=fare-value
print("Since There are ",n," persons You got 10% 
Discount")
print("Total Fare = ",n*total)
elif n>5 & n<=10:
disc=15
value=(fare*disc)/100
total=fare-value
print("Since There are ",n," persons You got 15% 
Discount")
print("Total Fare = ",n*total)
elif n>10 & n<=15:
disc=20
value=(fare*disc)/100
total=fare-value
print("Since There are ",n," persons You got 20% 
Discount")
print("Total Fare = ",n*total)
else:
disc=25
value=(fare*disc)/100
total=fare-value
print("Since There are ",n," persons You got 25% 
Discount")
print("Total Fare = ",n*total)
print("----------------------------------------")
print("Thank You, Visit Again")
