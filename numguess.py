# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:10:31 2022

@author: Simran-pc
"""

import random

num = random.randint(1, 10)
num2 = random.randint(1,5)
guess = None

print("your hint is",num+num2)
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")