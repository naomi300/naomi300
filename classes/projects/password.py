from lib2to3.pgen2.pgen import generate_grammar
from lib2to3.pytree import convert
import numbers
from operator import length_hint
from random import random
from sqlite3 import IntegrityError



import random
from tokenize import Number 
print("welcome to our password generator")
chr = 'Naomi1024'
#ask user number of password they want to generate
#convert num_password into intergers
#ask user for password length and convert length password to integer
#len_password
#print('here are your passwords')
number_password = int (input("write your preffered numbers"))
len_password = int(input("how many characters would you like"))
for password in range(number_password):
    password=''
    for c in range(len_password):
        password +=random.choice(chr)
    print(password)






 

