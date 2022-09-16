
# getting input from the user to replace a word

sentence = input("enter your sentence: ")
print("your sentence is: ", sentence)

first_word = input("enter the word to replace: ")
second_word = input("enter the word to replacce it with: ")

Replace = sentence.replace(first_word, second_word)

print(Replace)