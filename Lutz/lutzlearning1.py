import os #Used in line 12
import sys #Used in line 15
import threenames #Prints here and used in line 22
import math #Used on line 26
import random #Used on line 29

print('Hello World')

print(2 ** 8)
print('Spam' *8)

cwd = os.getcwd()
print(cwd)

print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)

#You can save the output of a file to a file using the > syntax in command line

print(threenames.b, threenames.c)
print(dir(threenames))
exec(open('threenames.py').read())

print(math.pi)
print(math.sqrt(85))

print(random.random())
print(random.choice([1, 2, 3, 4]))

S = 'shrubbery'
L = list(S)
print(L)
L[1] = 'c'
print(''.join(L))

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())

S = 'Spam'
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))

line = 'aaa,bbb,ccc,dd'
print(line.split(','))

S = 'spam'
print(S.upper())
print(S.isalpha())

line = 'aaa,bbb,cccc,dd\n'
print(line.rstrip())
print(line.rstrip().split(','))
