# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:52:01 2019

@author: sqcal
"""

word = list("anaconda")
RemainingAttempts = 5
tempword = []


for i in list(range(len(word))): 
    tempword.append('*')

def checkletter(letter):    
    if letter in word:
        print("{} is in the word!".format(letter))
        for i in list(range(len(word))):
            if word[i] == letter:
                tempword[i] = letter
        print(''.join(tempword))
    else: print("{} is Not in the word!".format(letter))
    
while RemainingAttempts > 0:
    print('Remaining attempts:{}'.format(RemainingAttempts))
    letter = input("please enter letter:")
    print('********************************************\n')
    checkletter(letter)
    if '*' not in tempword:
        print("Congradulations!")
        break
    RemainingAttempts = RemainingAttempts-1