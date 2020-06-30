print('H A N G M A N')
print('Guess the word: ')
word_list = ['python', 'java', 'kotlin', 'javascript']
word = input()
if word in word_list:
    print("You survived!")
else:
    print("You are hanged!")
