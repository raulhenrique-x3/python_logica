userInput = input().strip().lower()
userInputReverse = userInput[::-1]
arr = []
wordArr = []

stringSemEspaco = ''.join(userInputReverse.split()).capitalize()
wordArr.append(stringSemEspaco)
userInputSemEspaco = ''.join(userInput.split()).capitalize()

if userInputSemEspaco == wordArr[0]:
  print("VERDADEIRO")
else:
  print("FALSO")