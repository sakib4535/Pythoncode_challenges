import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 15
answer = random.randint(1,highest)
guess = 0
print(answer)

while guess != answer:
    print("Please Get the Correct $$Value$$ of the Coin Between 1 - {}: ".format(highest))
    guess = get_integer(": ")

    if guess == answer:
        print("You Guessed it Right First Time, You Have the NFT DATABASE Now in C:/Users?####!!")
        break
    else:
        if guess < answer:
            print("Please Guess the Higher Value of the Coin")
        else:
            print("Please Guess the Lower value of the Coin")
        guess = int(input())
        if guess == answer:
            print("Well Done, You Got the Right Valuation - $$####$$")
        else:
            print("Sorry, You Failed and Get Nothing @@")

