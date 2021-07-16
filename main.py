import os
import sys
import codecs
import time
import re
from sys import exit

from func import straddle, unstraddle, encrypt, decrypt, replacer, split_str, even, clear, constructWav, constructWavFromFile
clear()

# Variables
ciphertext = "No data available!"
deciphertexttext = "No data available!"
ePlaincode = "No data available!"
dePlaincode = "No data available!"
plaintext = "No data available!"


# Text menu
def print_menu():
    print (20 * "=" , "ONE-TIME PAD PYTHON FRAMEWORK" , 20 * "=")
    print ("[1] Encode plaintext \n[2] Decode plaincode to plaintext \n[3] Encrypt plaincode to ciphertext \n[4] Decrypt ciphertext to plaincode \n[5] Generate audio message of last ciphertext \n[6] Generate audio file from ciphertext.txt \n[7] Quit the program \n[8] Clear data from terminal ")
    print (20 * "=" , "Last Data" , 40 * "=")
    print ("[1]:\n" + ePlaincode)
    print ("[2]:\n" + dePlaincode)
    print ("[3]:\n" + ciphertext)
    print ("[4]:\n" + plaintext)
    print (71 * "=")

loop=True

while loop:

    print_menu()
    choice = input("\nWhat do you want to do? [1-8]: ")
   
    if choice == "1":
        clear()
        print (30 * "-" , "Encode text into decimal code" , 30 * "-")
        print ("*** Attention: This will generate a plaincode which is not protected by encryption! ***")
        print ("*** This program uses the checkerboard \"AT ONE SIR\" for encoding into decimal system. ***\n*** Characters outside of this checkerboard will not be accepted. ***")
        table =  ' | 0  1  2  3  4  5  6  7  8    9\n'
        table +=      " +--------------------------------\n"
        table +=      " | A  T     O  N  E     S  I    R\n"
        table +=     "2| B  C  D  F  G  H  J  K  L    О\n"
        table +=     "6| P  Q  U  V  W  X  Y  Z  F/L  SPC\n"
        print (table)

        O = input("Enter a text for encoding to plaincode: \n$ ") 
        ePlaincode = (straddle(O))
        # ePlaincode = (straddle(O), [("682268","682"),("686668","686"),(" ","")])
        if (ePlaincode):
            ePlaincode = ''.join(str(char) for char in ePlaincode)   
            ePlaincode = (" ".join(split_str(ePlaincode, 5))) 
            print("Plaincode:\n" + ePlaincode)
            print ("\nPlaincode decoded:\n" + "".join(unstraddle(ePlaincode.replace(" ", ""))))
        elif not (ePlaincode):
            ePlaincode = "No data available!"
        else:
            print ("huh")
        input("\nPress Enter to continue...\n")
        clear()

    elif choice=="2":
        clear()
        print ("*** Attention: This will generate a plaincode which is not protected by encryption! ***")
        print ("*** This program uses the checkerboard \"AT ONE SIR\" for encoding into decimal system. ***\n*** Characters outside of the this checkerboard will not be accepted. ***")
        table =  ' | 0  1  2  3  4  5  6  7  8    9\n'
        table +=      " +--------------------------------\n"
        table +=      " | A  T     O  N  E     S  I    R\n"
        table +=     "2| B  C  D  F  G  H  J  K  L    О\n"
        table +=     "6| P  Q  U  V  W  X  Y  Z  F/L  SPC\n"
        print (table)
        O = input("Input the plaincode for decoding to plaintext: \n$ ").replace(" ", "")
        if O:
            dePlaincode = "".join(unstraddle(O))
            print ("\nPlaintext:" + dePlaincode)
            input("\nPress Enter to continue...\n")
            clear()
        if not O:
            dePlaincode = "".join(unstraddle(O))
            dePlaincode = "No data available!"
            
    elif choice=="3":
        clear()
        print("*** Accepted input formats: *** \n format 1: 00000 00000 \n format 2: 0000000000")
        raw_message = input("\nEnter your plaincode to encrypt:\n$ ").replace(" ","")
        raw_key     = input("Enters the groups of your encryption one-time pad:\n$ ").replace(" ","")
        
        clear()
        ciphertext = encrypt(raw_message, raw_key)
       # print ("\nEncryption finished:\n" + ciphertext)
        input("\nPress Enter to return to Main Menu...")
        clear()
        
    elif choice=="4":
        clear()
        print("*** Accepted input formats: *** \n format 1: 00000 00000 \n format 2: 0000000000")
        raw_message = input("\nEnter the ciphertext to decrypt:\n$ ").replace(" ","")
        raw_key     = input("Enter the groups of your decryption one-time pad:\n$ ").replace(" ","")
        clear()
        plaintext = decrypt(raw_message, raw_key)
        input("\nPress Enter to return to main menu...")
        clear()

    elif choice=="5":
        clear()
        while (True):
            #constructWavFromFile("message.txt")
            #constructWav(message)
            constructWav((" ".join(split_str(ciphertext, 5))))
            print ("Audio ciphertext is assembled....")
            break
        print("ciphertext.wav was created successfully!")
        input("\nPress Enter to continue...")
        clear()
    
    elif choice=="6":
        clear()
        while (True):
            constructWavFromFile("ciphertext.txt")
            print ("Audio ciphertext is assembled....")
            break
        print("ciphertext.wav was created successfully!")
        input("\nPress Enter to continue...")
        clear()
        
    elif choice=="7":
        raise SystemExit()
    elif choice=="8":
        clear()
        ciphertext = "No data available!"
        deciphertexttext = "No data available!"
        ePlaincode = "No data available!"
        dePlaincode = "No data available!"
        plaintext = "No data available!"
        
    else:
       clear()
       input("This option does not exist. Press any key to continue...")
       clear()
