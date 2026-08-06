Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
#int float complex
a=12
type(a)
<class 'int'>
b = 13.4
type (b)
<class 'float'>
c = 12+4j
type(c)
<class 'complex'>
c = 12+6j
c
(12+6j)
#str list tuple
s = 'codegnan'
id(s)
1750982229936
s += 'python'
s
'codegnanpython'
id(s)
1750939174256
s='aaaaaaaa'
s
'aaaaaaaa'
type(s)
<class 'str'>
1 = [1,2,3,4,5,5,6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1 = [1,2,3,4,5,5,6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1 =[1,2,3,4,5,6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=[1,2,3,4,5,6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4,5,6]
type(1)
<class 'int'>
type(l)
<class 'list'>
id(l)
1750981195648
t=(1,2,3,4,5)
type(t)
<class 'tuple'>
t
(1, 2, 3, 4, 5)
t=(1,12.3,4,'c')
t
(1, 12.3, 4, 'c')
#set dict
s={80,70,24,14,25,78,78,78,78,78}
id(s)
1750981812384
s.add(20)
>>> s
{80, 20, 70, 14, 24, 25, 78}
>>> s.add(100)
>>> s
{80, 20, 100, 70, 14, 24, 25, 78}
>>> id(s)
1750981812384
>>> a={1,12.3,'str'}
>>> a
{1, 12.3, 'str'}
>>> set(s)
{100, 70, 14, 78, 80, 20, 24, 25}
>>> type(s)
<class 'set'>
>>> d={'productname' :'xyz' ,'price' :200, 'stock' :true}
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d={'productname' :'xyz' ,'price' :200, 'stock' :true}
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d = {'productname' : 'xyz' ,'price' : 200, 'stock' : True}
>>> s={1,2,3,4}
>>> 
>>> s=frozenset({2,2,4,5,5})
>>> s
frozenset({2, 4, 5})
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> a=()
>>> b=[]
>>> c={}
>>> s=''
>>> d=none
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> d=None
>>> type(d)
<class 'NoneType'>
