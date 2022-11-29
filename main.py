word = input("What word would you like to reverse? \n")
character = len(word)-1
for i in range(0,len(word)):
  print(word[character], end='')
  character = character-1
print('')