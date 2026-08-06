Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======= RESTART: C:/Users/HP/Desktop/PYTHON-COURSE-WORK/day 2/keyword.py =======
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> b
20
>>> b=30
>>> b
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> c
30
>>> b
30
>>> a,b,c
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,b,c
NameError: name 'a' is not defined
>>> b,c
(30, 30)
