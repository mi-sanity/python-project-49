#!/usr/bin/env python3

import prompt


def welcome_user():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print('Hello, ' + name + '!')
