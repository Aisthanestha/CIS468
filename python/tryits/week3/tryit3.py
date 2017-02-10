#!/usr/bin/env python3
'''
try:
        userInput=int(input('enter a number:'))
except ValueError:
        print('Not a valid Number!')
'''
try:
        a='1'+1
except TypeError:
        print('Type Error Occured')
try:
        import test
except SyntaxError:
        print('wow that shit you imported broke')
