import symbol

print(symbol)


import random

computer=["rock","paper","scissor"]

choice=random.choice(computer)


def rock_paper_scissor(computer,programmer):


    if programmer not in ["rock","paper","scissor"]:

        return symbol.options[4]

    elif programmer==computer:

        return symbol.options[2]+symbol.options[3]

    elif(programmer=="rock" and computer=="paper") or (programmer=="paper" and computer=="scissor") or (programmer=="scissor" and computer=="rock"):

        return symbol.options[1]+symbol.options[3]
    
    else:
        return symbol.options[0]+symbol.options[3]


programmer=input("Enter your choice: ").lower()

print("Computer choice is :",choice)

result=rock_paper_scissor(choice,programmer)
print(result)


    


