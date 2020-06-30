import random
print('H A N G M A N')
print('Guess the word: ')
word_list = ['python', 'java', 'kotlin', 'javascript']
words = random.choice(word_list)
word = input()
if words == "python":
    print("Guess the word pyt---:")
elif words == "java":
    print("Guess the word jav-")
elif words == "javascript":
    print("Guess the word jav-------:")
elif words == "kotlin":
    print("Guess the word kot---:")

if word == words:
    print("You survived!")
else:
    print("You are hanged!")
