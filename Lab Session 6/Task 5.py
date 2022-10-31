# Task 5
import random

def Encryption():
    SpaceNum = random.randint(2,20)

    Text = input("Please enter a string: ")
    NewText = Text.join(" ")
    print(NewText)

Encryption()