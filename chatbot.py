import os

temp = input("Please select language/Bitte Sprache auswählen：")
x = str(temp)

if x == 'de':
    os.system('python de.py')
else:
    if x == 'en':
        os.system('python en.py')
    else:
        print("invalid input")
