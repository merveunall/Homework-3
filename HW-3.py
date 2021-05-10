def reverse(s):
  str = ""
  for i in s:
    if(i!=' '):
         str = i + str
  return str.lower()

string = input("give me something \n")
reversedString = reverse(string)
print('\n'+reversedString)