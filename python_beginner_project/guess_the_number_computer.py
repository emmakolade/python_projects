import random

def guess(x):
    random_n = random.randint(1, x)

    n_guess = 0 # I set the number to quess to be zero, bcos i dont want it to be the quess num.


    while n_guess != random_n:
        n_guess = int(input(f"enter a guess number between 1 and {x} :"))
        if n_guess < random_n:
            print("sorry the guess is too low, try again: ")
        elif n_guess > random_n:
            print("sorry guess is too high, try  again: ")

    print(f" greattttt. you got the number {random_n}")

guess(10)



def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high: # there will be an error from .randint if the low and high is the same number
            n_guess = random.randint(low, high)
        else:
            n_guess = low # can also be high
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = n_guess - 1
        elif feedback == "l":
            low = n_guess + 1

    print(f" the computer guessed your number, {n_guess}, correctly")

computer_guess(10)