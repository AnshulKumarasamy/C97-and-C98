intro = input("enter your introduction:")
charCount = 0
wordCount = 1

for i in intro:
    charCount = charCount+1
    if(i == ' '):
        wordCount = wordCount+1

print("Number of word in the string:")
print(wordCount)
print("Number of characters in the string")
print(charCount)