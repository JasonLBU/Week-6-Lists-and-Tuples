# Task 2
def factors(n):
    return [i for i in range(1, n + 1) if not n % i]

Integer = int(input("Please enter an integer: "))
print(factors(Integer))