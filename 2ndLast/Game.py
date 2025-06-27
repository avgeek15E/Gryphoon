
# Rules
# 1. It should read your name
# 2. It should ask a question like (what is the square of number) number should be any number from 1 to 100
# 3. If users answer is right then score increases by 10
# 4. if wrong answer score decreases by 5
# 5. it should ask again and again
# 6. it should ask do you want to quit
# 7. if yes it should continue
# 8. if no it should display looser
# 9. it may ask what is the square root of a perfect square from 1 to 10000
# 10. keep tracking the time at the time of giving the player name
# 11. calculate the answering time of each question by player



import random
from datetime import datetime
import error

name = input("Enter your name")
print("The player name is ", name)
score = 0

while True:
    randomNumber = random.randint(1, 100)
    randomPNumber = randomNumber * randomNumber
    qList = [f"Enter the square of {randomNumber}", f"Enter the square root of {randomPNumber}"]
    question = random.choice(qList)

    print(question)
    currTime = datetime.now()
    userInput = int(input(f"Enter your answer"))

    square = pow(randomNumber, 2)
    squareRoot = pow(randomPNumber, 0.5)

    ansTime = datetime.now()
    if (userInput == square or userInput == squareRoot):
        score = score + 10
    else:
        score = score - 5

    print("Your score is ", score)
    period = ansTime - currTime
    print(f"You took {period.total_seconds()} seconds")

    print("Do you want to continue")
    print("Type yes to continue")
    ch = input()

    if (ch != "yes"):
        break

print("------------------------------------")
print(f"Your name is {name}")
print(f"Your score is {score}")
print(f"You are a LOOSER")

