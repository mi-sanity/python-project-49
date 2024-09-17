#!/usr/bin/env python3

def welcome_user():
    import prompt
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    if name != None:
        print('Hello, ' + name + '!')



