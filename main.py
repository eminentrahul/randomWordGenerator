import random
lengthOfWord = int(input("Enter the lenght of words: "))
numberOfWord = int(input("Enter the number of words: "))
firstLetter = input("Enter the first letter of the word: ")
lastLetter = input("Enter the last letter of the word: ")

wordList = []

for word in open('words_alpha.txt'):
    if len(word) == lengthOfWord+1 and word[0] == firstLetter and word[-2] == lastLetter:
        wordList.append(word[:lengthOfWord])

print(random.sample(wordList, numberOfWord))
                    
