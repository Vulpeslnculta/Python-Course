from random import randint

answer = randint(0, 10)

print("Your challenge is to guess a random number between 1 and 10 in two tries\n")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Oops, you've missed, bet higher next time!")
    else:
        print("Oops, you've missed, bet lower next time!")
    guess = int(input())
    if guess == answer:
        print("Good job mate! you've did it!")
    else:
        print("Sorry, but you didn't got the number :( ")
else:
    print("You are cheating or you are just that lucky? You got it first time!")
