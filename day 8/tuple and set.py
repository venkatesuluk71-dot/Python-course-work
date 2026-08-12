Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[-1]
True
t[-3]
{1, 2, 3}
t[2]
'str'
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t(-1:-3)
SyntaxError: invalid syntax
t(::-1)
SyntaxError: invalid syntax
t[-1:-3:-1]
(True, {1: 1, 2: 2})
True in t
True
false in t
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    false in t
NameError: name 'false' is not defined. Did you mean: 'False'?
False in t
False
bool in t
False
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t=(12,433,543,654,2434,65443,23)
t
(12, 433, 543, 654, 2434, 65443, 23)
sorted(t)
[12, 23, 433, 543, 654, 2434, 65443]
max(t)
65443
min(t)
12
len(t)
7
t
(12, 433, 543, 654, 2434, 65443, 23)
t.index(32)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t.index(32)
ValueError: tuple.index(x): x not in tuple
t.index(23)
6
t.index(2434)
4
t.count(23)
1
t.count(2434)
1
all((1,2,3))
True
all((1,2,3,00,0))
False
sum(t)
69542
any((00,2,3,4))
True
t = 1,2,3
t
(1, 2, 3)
a,b,c=t
a
1
b
2
c
3
# set
s = set()
type(s)
<class 'set'>
s ={1,2,3,4,454,54654,64533,644,434,323}
s
{1, 2, 3, 4, 323, 644, 454, 434, 64533, 54654}
s= {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(True)
s
{1, 12.3, 'str'}
#cant add list,set,dict into set
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(True)
s
{1, 12.3, 'str'}
a={1,2,3,4,5}
b={3,5,7,8,9}
2 in a
True
10 not in a
True
5 in b
True
5 not in c
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    5 not in c
TypeError: argument of type 'int' is not a container or iterable
5 not in b
False
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
b-a
{8, 9, 7}
a^b
{1, 2, 4, 7, 8, 9}
a*b
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a*b
TypeError: unsupported operand type(s) for *: 'set' and 'set'
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3}{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,7,8,9}<=a
False
a>=
SyntaxError: invalid syntax
a>={1,2}
True
a>={3,5,6}
False
a>={2,4,5}
True
a>={14,15}
False
m={1,2,3}
n{4,5,6}
SyntaxError: invalid syntax
n={4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a={12,23,32,42,2,23,32,3,111,3244,4,2,2,33}
sorted(a)
[2, 3, 4, 12, 23, 32, 33, 42, 111, 3244]
max(a)
3244
min(a)
2
len(a)
10
a.index(a)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
sum(a)
3506
a=a.copy()
a.add(20)
c
3
a={1,2,3}
b=a
b
{1, 2, 3}
a
{1, 2, 3}
a=a.copy()
a.add(20)
c
3
del a
a
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a
NameError: name 'a' is not defined
del b
a={1,2,3}
b=a
b
{1, 2, 3}
a
{1, 2, 3}
c=a.copy()
a.add(20)
c
{1, 2, 3}
any({True,0,1,2,3,()})
True
all({1,12,5,78})
True
any({0,''})
False
c.add(7)
c
{1, 2, 3, 7}
a
{1, 2, 3, 20}
a.add(10)
a
{1, 2, 3, 10, 20}
a.add(100)
a
{1, 2, 3, 100, 10, 20}
a.add(1004)
a
{1, 2, 3, 100, 10, 1004, 20}
a.add(04)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a.add(4)
a
{1, 2, 3, 100, 4, 10, 1004, 20}
>>> a.add({23,32,32,44})
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a.add({23,32,32,44})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> a.update({23,32,32,44})
>>> a
{32, 1, 2, 3, 100, 4, 10, 1004, 44, 20, 23}
>>> a.pop
<built-in method pop of set object at 0x0000020B24D42880>(
>>> a.pop()
32
>>> a.pop()
1
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
>>> a.remove(1004)
>>> a
{2, 3, 100, 4, 10, 44, 20, 23}
>>> a.remove(100)
>>> a
{2, 3, 4, 10, 44, 20, 23}
>>> a.discard(100)
>>> a
{2, 3, 4, 10, 44, 20, 23}
>>> a.discard(30)
>>> a
{2, 3, 4, 10, 44, 20, 23}
>>> a.discard(10)
>>> a
{2, 3, 4, 44, 20, 23}
>>> a.clear ()
>>> a
set()
>>> a=frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
