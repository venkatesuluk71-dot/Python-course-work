Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f=20.3
int(f)
20
complex(f)
(20.3+0j)
bool(f)
True
str(f)
'20.3'
c=12+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(12+3j)'
bool(c)
True
float(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
s='codegnan'
a='3456'
int(s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(a)
3456
float(a)
3456.0
bool(s)
True
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'a', 'e', 'o', 'n', 'g', 'c', 'd'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l=[1,3,4,5,6,7,8]
int(l)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 3, 4, 5, 6, 7, 8]'
tuple(l)
(1, 3, 4, 5, 6, 7, 8)
set(l)
{1, 3, 4, 5, 6, 7, 8}
bool(l)
True
dict(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
dict
<class 'dict'>
dict(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
tuple(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    tuple(1,2,3,4,5)
TypeError: tuple expected at most 1 argument, got 5
tuple=(1,2,3,4,5)
str(t)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    str(t)
NameError: name 't' is not defined
str(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    str(t)
NameError: name 't' is not defined
str(tuple)
'(1, 2, 3, 4, 5)'
list(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(t)
NameError: name 't' is not defined
list(tuple)
[1, 2, 3, 4, 5]
set(tuple)
{1, 2, 3, 4, 5}
bool(tuple)
True
dict(tuple)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(tuple)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> int(tuple)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(tuple)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> dict={1:1,2:2,3:3}
>>> str(dict)
'{1: 1, 2: 2, 3: 3}'
>>> list(dict)
[1, 2, 3]
>>> tuple(dict)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    tuple(dict)
TypeError: 'tuple' object is not callable
>>> del tuple
>>> tuple(dict)
(1, 2, 3)
>>> bool=true
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    bool=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> bool=True
>>> int(bool)
1
>>> float(bool)
1.0
>>> str(bool)
'True'
>>> list(bool)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list(bool)
TypeError: 'bool' object is not iterable
>>> #it cant convert into list dict tuple
