# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:24:22 2019

"""

import time

# open the enable1 dictionary as set
with open('enable1.txt') as file:
    dictionary = [line.replace('\n','') for line in file.readlines()]
    dictionary = set(dictionary)

# create a set of the letters in the alphabet
alphabet = set('abcdefghijklmnopqrstuvwxyz')

def SpellingBeeSearch(letters):
    startTime = time.time()
    # create an alphabet string without spelling bee letters
    badLetters = ''
    for letter in alphabet:
        if letter not in letters:
            badLetters += letter
    # find words matching the criteria
    words = []
    for word in dictionary:
        if len(word) > 3:
            if letters[0] in word:
                if any(letter in word for letter in badLetters):
                    pass
                else:
                    words.append(word)
    words.sort()    
    print('--- %2.4f seconds ---' % (time.time() - startTime))
    return words
