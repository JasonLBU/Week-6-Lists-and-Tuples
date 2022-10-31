# Task 3
def PrimeNumber():
    Number = int(input("Please enter a number: "))
    for i in range(2, Number):
        if (Number % i) == 0:
            Flag = True
            break
        else:
            Flag = False
    if Flag:
        print(str(Number) + " is not a prime number")
    else:
        print(str(Number) + " is a prime number")

PrimeNumber()