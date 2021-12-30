
print("Welcome to The Password Generator by Jack McLean ")
print(" The Password Generator by Jack McLean Version 1.0 ")
print("***************************************************")
print("What is your name?")
firstname = input()

print("Hello,", firstname)

print("Welcome to the password generator made by S8msGITcode")
print("***************************************************")

import random

print('''
Password Generator
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

print('How long should your password be? Type it out in digits.')

print("***************************************************")
length = input('password length?')
length = int(length)

print('Here are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
  password =input

print("Thank you for using Simple Password generator :) ")
