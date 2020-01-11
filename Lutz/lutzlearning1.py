import os #Used in line 17
import sys #Used in line 20
import threenames #Prints here and used in line 27
import math #Used on line 31
import random #Used on line 34
import re #Used on line 68
import struct #Used on line 207
import codecs #Used on line 240
import decimal # used in line 261
from fractions import Fraction # used in line 265

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

print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
#match.group(1)
match = re.match('[/:](.*)[/:](.*)[:/](.*)','/usr/home:lumberjack')
match.groups()
print(re.split('[/:]','/usr/home/lumberjack'))

L = [123, 'spam', 1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4,5,6])
print(L * 2)
print(L) #We didn't change the original list
L.append('NI')
print(L)
L.pop(2)
print(L)
M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

M = [[1,2,3],
[4,5,6],
[7,8,9]]
print(M)
print(M[1])
print(M[1][2])

#col2 = [row[1] for row in M]
#print(col2)

#print([row[1] + 1 for row in M])
#print([row[1] for row in M is row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'spam']
print(doubles)
print(list(range(4)))
print(list(range(-6,7,2)))
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x/2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print({sum(row) for row in M})
print({i : sum(M[i]) for i in range(3)})

print([ord(x) for x in 'spaam'])
print({ord(x) for x in 'spaam'})
print({x: ord(x) for x in 'spaam'})
print((ord(x) for x in 'spaam'))

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['quantity'])
D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],
'age': 40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'][-1])
rec['jobs'].append('janitor')
print(rec)
value = rec.get('name', 'no name') #second argument is a default value

D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -=1

#these two are equivalent
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print(squares)

T = (1, 2, 3, 4)
print(len(T))
print(T + (5,6))
print(T[0])
print(T.index(4))
print(T.count(4))
print(T[0])
T = (2,) + T[1:]
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])

f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()
f = open('data.txt') #no mode defaults to 'r'  or read mode
text = f.read()
print(text)
print(text.split())
for line in open('data.txt'): print(line)
print(dir(f))
f.close()

'''
#this is returning an error regarding number of arguments expected by struct.pack
packed = struct.pack('>4ish', 7, b'spam', 8)
print(packed)
file = open('data.bin', 'wb')
file.write(packed)
file.close()
data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>4ish', data))
'''

S = 'sp\xc4m'
print(S)
print(S[2])
file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()
text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text))
raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))
print(text.encode('utf-8'))
print(raw.decode('utf-8'))
print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))

#for 2.x
print(codecs.open('unidata.txt', encoding='utf8').read())
print(open('unidata.txt', 'rb').read())
print(open('unidata.txt').read())

X = set('spam')
Y = {'h', 'a', 'm'}
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)
print({n ** 2 for n in [1, 2, 3, 4]})

print(list(set([1, 2, 1, 3, 1])))
print(set('spam') - set('ham'))
print(set('spam') == set('asmp'))
print('p' in set ('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1/3)
print((2/3) + (1/2))
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
print(1 > 2, 1 < 2)
print(bool('spam'))
X = None
print(X)
L = [None] * 100
print(L)

print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print('yes')

if type(L) == list:
    print('yes')

if isinstance(L, list):
    print('yes')

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)
