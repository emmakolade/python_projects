# building a login/signup system
# this program will detect whether a password and username is right or wrong

create_account = input("press ENTER to create your account")

username = input("enter your username: ")
password = input("enter password: ")

print(" account created successfully")

print("you can now login")

username1 = input("enter username to login: ")
password1 = input("enter password: ")

if username == username1 and password == password1:
    print("Login successful!")
elif username != username1 and password != password1:
    print("invalid input: username or password incorrect")
elif username != username1:
    print("invalid username, try again")
elif password != password1:
    print("invalid password, try again")



