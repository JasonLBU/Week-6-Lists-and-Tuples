#Task 1
def PositiveInteger(Decimal):
    BinaryNum = bin(Decimal)
    return BinaryNum


Number = int(input("Please enter a positive integer: "))
if isinstance(Number, int):
    print("Valid N5umber")
    print("Your number in binary form is", PositiveInteger(Number))
else:
    print("Invalid Number")
