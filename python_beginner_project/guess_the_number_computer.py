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