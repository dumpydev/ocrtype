from colorama import init, Fore, Back, Style
import os
from time import sleep
from PIL import Image
import pytesseract
import keyboard
init()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(Fore.GREEN)
print('''
 ▒█████   ▄████▄   ██▀███     ▄▄▄█████▓▓██   ██▓ ██▓███  ▓█████ 
▒██▒  ██▒▒██▀ ▀█  ▓██ ▒ ██▒   ▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓█   ▀ 
▒██░  ██▒▒▓█    ▄ ▓██ ░▄█ ▒   ▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒███   
▒██   ██░▒▓▓▄ ▄██▒▒██▀▀█▄     ░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒▒▓█  ▄ 
░ ████▓▒░▒ ▓███▀ ░░██▓ ▒██▒     ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░▒████▒
░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░     ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░░ ▒░ ░
  ░ ▒ ▒░   ░  ▒     ░▒ ░ ▒░       ░     ▓██ ░▒░ ░▒ ░      ░ ░  ░
░ ░ ░ ▒  ░          ░░   ░      ░       ▒ ▒ ░░  ░░          ░   
    ░ ░  ░ ░         ░                  ░ ░                 ░  ░
         ░                              ░ ░                     
''')
print(Fore.RED)
flist = []
os.scandir('.')
for file in os.scandir('.'):
    if file.name.endswith('.png') or file.name.endswith('.jpg'):
        flist.append(file.name)
    else:
        continue

if len(flist) == 0:
    print("No images found in current directory.")
    manual = input("Would you like to manually enter the path to the image? (y/n): ")
    if manual == 'y':
        path = input("Enter the path to the image: ")
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
        print(text)
        exit()
    else:
        print("Exiting...")
        exit()
elif len(flist) == 1:
    print("Only one image found in current directory. Using it.")
    text = pytesseract.image_to_string(Image.open(flist[0]))
    print("OCR: " + text)
else:
    print("Select an image to OCR:")
    for i in range(len(flist)):
        print(f"{i}: " + flist[i])
        print("OCR: " + pytesseract.image_to_string(Image.open(flist[i])))
    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice >= len(flist):
                print("Invalid choice.")
                continue
            else:
                break
        except ValueError:
            print("Invalid choice.")
            continue
    text = pytesseract.image_to_string(Image.open(flist[choice]))
    print("OCR: " + text)
print("Starting in 5 seconds. Press Ctrl+C to cancel.")
for i in range(0,5):
    print("Starting in " + str(5-i) + " seconds.")
    sleep(1)
for i in range(0, len(text)):
    keyboard.write(text[i])
    sleep(0.03)
    print("Writing: " + text[i])

print("Done.")
print("Github: @dumpydev\nTelegram: @flandolf")