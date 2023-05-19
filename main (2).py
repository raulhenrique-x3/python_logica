userInput2 = input().strip()
userInputReverse = userInput2[::-1]
arr = []

for word in userInput2:
  arr.append(word[::-1])
reversedNoVirg = ''.join(arr)
print(reversedNoVirg[::-1])