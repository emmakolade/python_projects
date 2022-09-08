# Madlibs using string concatenation

# there are few ways to do concatention

# print(f"my name is {Name}")
# print("my name is {}".format(Name))
# print(f"my name is " + name)

MADLIB = input("this is a madlib game, press enter to start")

food = input("enter any special meal: ")
market = input("enter any market of your choice: ")
transport = input("enter your transportation means: ") # either a bike, car, bus or train
friend = input("enter your friends name: ")

madlib = f" You can make {food}, in different ways. the only thing is that you have to master a recipe. \
You also have to go to {market} to get some ingredient for your meal,\n \
now take a {transport} to the market, get whatever you want to get so that you can do other things.\n Also you can decide to go visit {friend} after your market activities"

print(madlib)
