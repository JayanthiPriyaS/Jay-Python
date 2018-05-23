char=raw_input("Enter character:")
smallCase='abcdefghijklmnopqrstuvwxyz'
upperCase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#smallCase=range('a','z')
#upperCase=range('A','Z')

#if(ord(char) in range(65,92) or ord(char) in range(97,123)):
if( ord(char) in range(65,123) and ord(char) not in range(92,98)):  
  print("Character is an alphabet")
else:
    print("Character is a special Character")   



''' if((char in smallCase)or (char in upperCase)) :
    print("Character is an alphabet")
else:
    print("Character is a special Character") '''


''' if((char not in smallCase)or (char not in upperCase)) :
    print("Character is a special Character")
else:
    print("Character is an alphabet")   '''
