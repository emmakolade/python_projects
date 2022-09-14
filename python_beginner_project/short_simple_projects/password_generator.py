import random

print("Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!!@#$%^&*()_+-=`,.1234567890"

count = int(input("input amount of password to generate: "))  # how many password to generate

length = int(input("enter your password length: "))  # length of the password

print(" here are your passwords\n")

# to get the passwords the user needs
for password in range(count):
    passwords = " "
    for chars in range(length):
        passwords += random.choice(characters)

    print(passwords)
