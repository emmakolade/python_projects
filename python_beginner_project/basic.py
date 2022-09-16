char_name = "James "
char_age = "57"
is_man = True

print(char_name + "is 28 years old")
print("he loves MO")

char_name = "kay"
print("he liked the name " + char_name)
print("but he deosnt like being " + char_age)

# mathematics
from math import *

num = -5
print(abs(num))
print(str(num) + " five number")
print(pow(4, 7))
print(max(4, 9))
print(min(4, 9))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(25))

# getting input from users
name = input("enter your name now:")
age = input("enter your age")
print("Hello " + name + "!, How are you doing today")
print("you are" + age + "years old")

# building a basic calculator
first_number = input("enter a number: ")
second_number = input("enter a another number: ")
res = float(first_number) + float(second_number)

print(res)

# mad libs game

color = input("enter a color: ")
plural_noun = input("enter a noun: ")
celeb = input("enter a celeb: ")

print("roses are " + color)
print(plural_noun + " are blue")
print("I love " + celeb)

# lists
friends = ["MO", "Black", "Yoyo"]
friends[1] = "Kolade"

print(friends[0])
print(friends[0:2])

# lisit functions

lucky_numbers = [4, 7, 8, 34, 67, 35]
friends = ["MO", "Black", "Bukola", "Yoyo", "james"]
friends.sort()  # .reverse
friends2 = friends.copy()
friends.insert(1, "Eben")
print(friends.index("MO"))
friends.remove("MO")
friends.extend(lucky_numbers)
friends.append("Uzoma")
friends.pop()
print(friends.count("MO"))
print(friends)

# tuples
coordinates = (5, 8)  # they cant be changes or modified

print(coordinates[1])


# functions
def say_hello():
    print("hello Kolade")


say_hello()


def say_hi(name, age):
    print("Hi " + name + " your are " + str(age) + " old")


say_hi('Kolade', 27)


# return Statement

def xcube(num):
    return num * num * num


res = xcube(5)
print(res)

# if statements

is_this_male = True
is_tall = False

if is_this_male or is_tall:
    print("you be male joor or tall or both ")
elif is_this_male and not (is_tall):
    print("you are a short male")
elif not (is_this_male) and (is_tall):
    print("you are not a male but are tall")
else:
    print("you are neither")


# create a function that gives the max num passed into it,
# takes 3 parameters and return the largest
def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print("n1 is the largest")
    elif n2 >= n1 and n2 >= n3:
        print("n2 is the largest")
    else:
        print("n3 is the greatest")


max_num(4, 6, 9)
# building a more advance calculator

first_n = float(input("enter first number: "))
operator = input("enter operator: ")
snd_n = float(input("enter second number"))

if operator == '+':
    print(first_n + snd_n)
elif operator == "-":
    print(first_n - snd_n)
elif operator == "/":
    print(first_n / snd_n)
elif operator == "*":
    print(first_n * snd_n)
else:
    print("invalid operator")

# dictionaries
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "un",
    1: "do"
}

print(month_conversions["Nov"])
print(month_conversions[0])
print(month_conversions.get("Dec"))
print(month_conversions.get("Love", "not a valid key"))

# while loop

i = 1
while i <= 15:
    print(i)
    i += 1

# building a guessing game

secret_word = "kolade"
guess = ""
count = 0
limit = 4
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if count < limit:
        guess = input("enter a guess word: ")
        count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you are out of guesses and you lose")
else:
    print("you are correct!")

# for loop
group = ["koladw", "MO", "Black"]

for letter in group:
    print(letter)

for index in range(len(group)):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(5):


# exponent function
def rasie_to_power(base, power):
    res = 1
    for i in range(power):
        res *= base
    return res


print(rasie_to_power(2, 4))

# 2d lists and Nested for loop

twod_list = [
    [1, 2, 4],
    [3, 5, 7],
    [6, 8, 9],
    [0]
]

print(twod_list[0][1])

for r in twod_list:
    print(r)
    for col in r:
        print(col)

# try except block

try:
    text = float(input("enter a number"))
    print(text)
except:
    print("invalid input")
# try except block

try:
    division = 10 / 0
    text = float(input("enter a number"))
    print(text)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)

employees = open("app.txt", "r")
print(employees.read())
print(employees.readline())
print(employees.readable())
employees.close()

employees = open("app.txt", "a")
employees.write("\nbukola - HR/Admin")
employees.close()

