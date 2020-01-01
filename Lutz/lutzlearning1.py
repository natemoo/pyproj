import os #Used in line 13
import sys #Used in line 16
import threenames #Prints here and used in line 23
import math #Used on line 27
import random #Used on line 30
import re #Used on line 66

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

D = {'food' }
