# Task 4
def Encryption():
    Text = input("Please enter a string: ")
    NoSpace = Text.strip()
    EncryptedText = NoSpace[::-1]
    print("Your encrypted text is: " + EncryptedText)

Encryption()