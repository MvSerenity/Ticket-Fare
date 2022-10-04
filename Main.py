print("Welcome to Conter No.1")
print("Price of per ticket is 2000rs")
print("----------------------------------------")

n = int(input("Enter the number of person(s): "))
fare = 2000

def discount(n):
    if n <= 5:
        return 10
    elif n <= 10:
        return 15
    elif n <= 15:
        return 20
    elif n >= 15:
        return 25
    
def total(n):
    return n * fare

def discount_total(n):
    return total(n) - int(total(n) * discount(n) / 100)


print("Total amount is: ", total(n))
print("Discount is: ", discount(n))
print("Total amount after discount is: ", discount_total(n))
print("----------------------------------------")
print("Thank You, Visit Again")
