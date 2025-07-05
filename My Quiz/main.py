import random

name = input("Enter the user name")

randomNumber = random.randint(1, 100)
randomPNumber = randomNumber * randomNumber

samples = [f"Enter the square of {randomNumber}", f"Enter the square root of {randomPNumber}"]
question = random.choice(samples)

print(question)
try:
    userInput = int(input("Enter your answer"))
except:







