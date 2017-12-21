import random
n = int(input("Enter the lenght of words: "))
w = int(input("Enter the number of words: "))
fl = input("Enter the first letter of the word: ")
lastLetter = input("Enter the last letter of the word: ")

wordList = []

for word in open('words_alpha.txt'):
    if len(word) == n+1 and word[0] == fl and word[-2] == lastLetter:
        wordList.append(word[:n])

print(random.sample(wordList, w))
                    
