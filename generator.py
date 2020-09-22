__author__ = 'Luka Marjanović'

import random
import time

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
syms = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def random_letter(letters):
    letter = random.choice(letters)
    return letter

def random_symbol(syms):
    sym = random.choice(syms)
    return sym

def random_number():
    num = random.randint(0, 9)
    return str(num)

def make_pass():
    letters_list = []
    nums_list = []
    syms_list = []

    for i in range(6):
        n = random.randint(0, 100)
        if n % 2 == 0:
            letters_list.append(random_letter(letters).lower())
        elif n % 2 != 0:
            letters_list.append(random_letter(letters).upper())

    for i in range(3):
        nums_list.append(random_number())

    for i in range(2):
        syms_list.append(random_symbol(syms))

    l = ''.join(letters_list)
    n = ''.join(nums_list)
    s = ''.join(syms_list)

    global password
    password = l, n, s
    password = ''.join(password)
    pass_list = list(password)
    random.shuffle(pass_list)
    password = ''.join(pass_list)

    return password