#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import sys
import codecs
import os
import math
import time
import wave
import random
import re
from functools import reduce

import os.path
import configparser

T = [["68", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
     ["",   "A", "T", "", "O",  "N", "E", "", "S",  "I", "R"],
     ["2",  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M"],
     ["6",  "P", "Q", "U", "V", "W", "X", "Y", "Z", "/", " "]]

def straddle(s):
    if not (s):
        clear()
        print ("ERROR:You didn't input anything!")
        #return "error"
    if (s):
        time.sleep(1)
        clear()
        straddle = "".join(L[0]+T[0][L.index(c)] for c in s.upper() for L in T if c in L)
        # Ugly workaround for an ungly bug... 
        straddle = replacer(straddle, [("682268","682"),("686668","686"),(" ","")]).ljust(300, '8')
        if len(straddle) == 300:
            plaincode = ''.join(str(char) for char in straddle)   
            plaincode = (" ".join(split_str(straddle, 5))) 
            return straddle
        elif len(straddle) > 300:
            print ("ERROR: Encoded text is", len(straddle), "characters long (defined limit is 300). Shorten your text")
        elif len(straddle) < 300:
            print("ERROR: Please check the data you've provided...")
        else:
            print("ERROR: Please check the data you've provided...")
 
def unstraddle(s):
# if len(s) == 300:
    if (s):
        s = iter(s)
        for c in s:
            if c in [T[2][0], T[3][0]]:
                i = [T[2][0], T[3][0]].index(c)
                n = T[2 + i][T[0].index(s.__next__())]
                yield s.__next__() if n == "/" else n
            else:
                yield T[1][T[0].index(c)]
    elif not (s):
        clear()
        print ("ERROR:You didn't input anything!")
        input("\nPress Enter to continue...\n")
        clear()
    else:
        print("ERROR: Please check the data you've provided...")

def encrypt(first, second):
    # ---- Regex to get only numeric characters ---- #
    first = re.sub("[^0-9]", "", first)
    second = re.sub("[^0-9]", "", second)
    
    # --- Convert the key and plaincode to a list ---- #
    first = [int(x) for x in str(first)]
    second = [int(x) for x in str(second)]
    
    third = []
    a = len(first)
    b = int(0)
    # ---- or for exact lenght "if (first) and (second) and len(first) == len(second):" ---- #
    if (first) and (second) and len(first) == 300 and len(second) == 300:
        while True:
            x = first[b]
            y = second[b]
            ans = (x - y)%10
            third.append(ans)
            b = b + 1
            # ---- or for exact lenght "if len(first) != 3 or len(second) != 3:" ---- #
            if len(first) == len(second):
                    if b == a:
                        print ("Performing Modulo 10 operation:")
                        print (first)
                        print("(-)")
                        print (second)
                        print("(=)")
                        print (third)  
                        third = ''.join(str(c) for c in third)
                        ''' split
                        third = (" ".join(split_str(third, 5)))
                        '''
                        time.sleep(1)
                        print ("\nEncryption finished:\n" + third)
                        break
            else:
                print ("ERROR! Something went very wrong...")
                return "No data available!"
    elif not (first) or not (second):
        print("ERROR: The OTP key or plaincode is empty...")
        return "No data available!"
    elif len(first) != 300 or len(second) != 300:
        print("ERROR: Plaincode and OTP key should be exactly 300 characters long.")
        return "No data available!"
    elif not len(first) == len(second):
        print("ERROR! The OTP key and plaincode message are not of an equal lenght!")
        return "No data available!"
    else:
        print("ERROR: Please check the data you've provided...")
        input("\nPress Enter to continue...")
        return "No data available!"
    encryptedText = ''.join(str(char) for char in third)   
    return (" ".join(split_str(encryptedText, 5)))  

def decrypt(first, second):
    # ---- Regex to get only numeric characters ---- #
    first = re.sub("[^0-9]", "", first)
    second = re.sub("[^0-9]", "", second)
    
    # --- Convert the key and plaincode to a list ---- #
    first = [int(x) for x in str(first)]
    second = [int(x) for x in str(second)]
    
    third = []
    a = len(first)
    b = int(0)
    if (first) and (second) and len(first) == 300 and len(second) == 300:
        while True:
            x = first[b]
            y = second[b]
            ans = (x + y)%10
            third.append(ans)
            b = b + 1
            if len(first) == len(second):
                    if b == a:
                        print ("Performing Modulo 10 operation:")
                        print (first)
                        print("(+)")
                        print (second)
                        print("(=)")
                        print (third)
                        third = ''.join(str(c) for c in third)
                        ''' split
                        third = (" ".join(split_str(third, 5)))
                        '''
                        time.sleep(1)
                        print ("\nDecryption finished:\n" + third)
                        break
            else:
                print ("ERROR! Something went very wrong...")
                return "No data available!"
    elif not (first) or not (second):
        print("ERROR: The OTP key or plaincode is empty...")
        return "No data available!"
    elif len(first) != 300 or len(second) != 300:
        print("ERROR! of Plaincode and OTP key should be exactly 300 characters long.")
        return "No data available!"
    elif not len(first) == len(second):
        print("ERROR! The OTP key and plaincode message are not of an equal lenght!")
        return "No data available!"
    else:
        print("Unexpected error! Please check the data you've provided...")
        input("\nPress Enter to continue...")
        return "No data available!"
    encryptedText = ''.join(str(char) for char in third)   
    return (" ".join(split_str(encryptedText, 5))) 

def replacer(text, replacements):
    return reduce(
        lambda text, ptuple: text.replace(ptuple[0], ptuple[1]), 
        replacements, text
    )

def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def even(num):
    if (num % 5) == 0:
       return("True".format(num))
    else:
       return("False".format(num))

def clear():
    '''
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    '''
    os.system('cls||echo -e \\\\033c')
    
# --- Convert message to audio section --- #
configFile = "default.ini"
if (len(sys.argv) > 1):
	# if arguments present
	configFile = sys.argv[1]

	if not configFile.endswith(".ini"):
		configFile = configFile + ".ini"

config = configparser.ConfigParser()
config.read(configFile)

audio_prepend                 = config.get('audio', 'prepend')
audio_append                  = config.get('audio', 'append')

# Message to synthesize and broadcast
message = "123456789 abcdefghijklmnopqrstuvwxyz"
loadFromFile = True

# Sounds for digits/numbers.
sounds = ["zero.wav", "one.wav", "two.wav", "three.wav", "four.wav", "five.wav", "six.wav", "seven.wav", "eight.wav", "nine.wav"]


# Sounds for alphanumeric. Use NATO Phonetic
alpha = ["alpha", "bravo", "charlie", "delta",  "echo", "foxtrot", "golf",
		"hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar",
		"papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor",
		"whiskey", "x-ray", "yankee", "zulu"]


def main():

	print("PyNumberStation started...")
	print("Load configuration from %s" % configFile)

	
	for x in range(0, len(message)):
		print(str(message[x]))
	

	if (os.path.isfile(sys.path[0] + "/vo/phonetic/alpha.wav") == False):
		print("Synthesis Failure: NO ALPHANUMERIC SUPPORT")
		time.sleep(5)

	return

def constructWavFromFile( fileName):
	fMsg = open(sys.path[0] + "/" + fileName, 'r')
	strMessage = fMsg.read()
	constructWav( strMessage )

	return

def getVO( character ):
	if character.isdigit() == True:
		return sounds[int(character)]
	else:
		if character == ',' or character == ' ':
			return "_blank.wav"
		if character == '.':
			return "_period.wav"
		if character == '\n':
			return "_end.wav"
			return

		if character.isalpha() == True:
			return "/phonetic/" + str(alpha[ord(character) - ord('a')] + ".wav")


def constructWav( strMessage ):

	print("Creating audio..")

	infiles = []

	strMessageOut = strMessage

	# determine infiles for message.
	for file in audio_prepend.split(","):
		if not file[0] == "/" or not file[0] == ".":
			file = sys.path[0] + "/" + file

		if os.path.exists(file):
			infiles.append(file)
		else:
			print  ("File %s not exists ... skipped!" % file)

	for character in strMessageOut:
		char_sound = sys.path[0] + "/vo/" + getVO(character)
		infiles.append(char_sound)
		print (char_sound)

	for file in audio_append.split(","):
		if not file[0] == "/" or not file[0] == ".":
			file = sys.path[0] + "/" + file

		if os.path.exists(file):
			infiles.append(file)
		else:
			print  ("File %s not exists ... skipped!" % file)

		infiles.append(file)

	infiles.append(sys.path[0] + "/vo/_comma.wav")

	outfile = sys.path[0] + "/cipher.wav"
	data    = []

	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])

	for x in range(0, len(infiles)):
		output.writeframes(data[x][1])

	#output.writeframes(data[0][1])
	#output.writeframes(data[1][1])
	#output.writeframes(data[2][1])
	output.close()

	print("Audio creation completed...")

	return
