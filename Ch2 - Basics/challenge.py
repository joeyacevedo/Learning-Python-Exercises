exit = False

while exit != True:
  cleanString = ''
  testString = input("Enter string to test for palindrome or 'exit'>>")

  if testString == 'exit':
    exit = True
    break

  testString = testString.lower()

  for l in testString:
    if l.isalnum():
      cleanString += l

  reverseString = cleanString[::-1]

  if testString == reverseString:
    print("True")
  else:
    print("False")
