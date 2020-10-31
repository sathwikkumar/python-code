from playsound import playsound
import time
import pyttsx3 as pyttsx

MORSE_DICT = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}  ##dictionary for morse code##

print('Morse code Translator')
def Text_to_Morse():
    text = input('Enter Text to Convert to Morse: ')       ##function to change the text to morse code##
    code = [MORSE_DICT[i.upper()] + ' ' for i in text if i.upper() in MORSE_DICT.keys()]
    morse=''.join(code)
    print(morse)
    for m in morse:
        if m=='.':
            playsound('F:\AC ORIGINS\python 3.85\dit.wav')
        elif m=='-':                                                   ##plays the sound for dit and dah##
            playsound('F:\AC ORIGINS\python 3.85\dah.wav')
        else:
            time.sleep(0.5)

def Morse_to_Text():                             ##function to change the morse to text##
    text = input('Enter Morse to Convert to Text: ')
    code = [k for i in text.split() for k,v in MORSE_DICT.items() if i==v]
    newtext = ''.join(code)
    print(newtext)
    engine = pyttsx.init()                 ##initializes the pyttsx to speak the word##
    engine.say(newtext)
    engine.runAndWait()

print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')             ##displays the options to user##

while True:
    try:
        selection = int(input("Enter Your Choice: "))
        if selection == 1:
            print(Text_to_Morse())
        elif selection == 2:
            print(Morse_to_Text())
        elif selection == 3:
            print('Exiting')
            break
        else:
            print("Wrong Selection, enter again")
    except:
        print("Wrong Selection, enter again")
