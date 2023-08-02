import random 
randomNumber = random.randint(1,20)
score =20
attempts = 0

def guess_game():

    guessedNumber = int(input("Guess the number between 1 and 20: "))

    print("randomNumber:",randomNumber)
    print("guessedNumber:",guessedNumber)

    if guessedNumber == randomNumber:
        print("Congratulations,you guessed the number in {attempts} attempts!")
    elif guessedNumber > randomNumber:
        print("Too High! Try again.")
    elif guessedNumber < randomNumber:
        print("Too low! Try again.")
    else:
        print("wrong guess!!!")

guess_game()