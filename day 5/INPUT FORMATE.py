Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #input formate
>>> #int float complex str list tuple set dict bool
>>> a=input
(
>>> a=input()
codegnan
>>> a
'codegnan'
>>> a=input()
1234
>>> a
'1234'
>>> a=input("enter the value")
enter the value 345676887787
>>> a
' 345676887787'
>>> marks=input("enter the marks:")
enter the marks:90
>>> marks
'90'
>>> marks=int(input("enter the marks:"))
enter the marks:90
>>> marks
90
>>> price = float(input("enter the price"))
enter the price78.54
>>> price
78.54
>>> cgpa = float(input("enter the cgpa:"))
enter the cgpa:9.98
>>> cgpa
9.98
>>> names=input("entre the names:")
entre the names:usha mummy vms
>>> names
'usha mummy vms'
>>> names.split()
['usha', 'mummy', 'vms']
>>> names.split(',')
['usha mummy vms']
course='python-java-c-c
SyntaxError: unterminated string literal (detected at line 1)
course='python-java-c-c++'
course.split()
['python-java-c-c++']
course
'python-java-c-c++'
course.split(',')
['python-java-c-c++']
course.split(-)
SyntaxError: invalid syntax
course.split('-')
['python', 'java', 'c', 'c++']
names = input("enter the numbers:")
enter the numbers:mummy ush
names
'mummy ush'
names = input("enter the numbers:").split()
enter the numbers:mummy ush
names
['mummy', 'ush']
names = int(input("enter the numbers:").split())
enter the numbers:ush usha
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names = int(input("enter the numbers:").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
names = int(input("enter the numbers:").split())
enter the numbers:ush venky
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    names = int(input("enter the numbers:").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
names = tuple(input("enter the numbers:").split())
enter the numbers:ush usha
names
('ush', 'usha')
# map() used to change the datatype inside the list by iterating one by one,it has two parameters,map(datatypes,what to convert
marks=input().split()
12 38 54 44
marks
['12', '38', '54', '44']
map(int,marks)
<map object at 0x000001F19A145A40>
list(map(int,marks))
[12, 38, 54, 44]
marks=list(map"(int,input("enter the marks").split()))
           
SyntaxError: unterminated string literal (detected at line 1)
marks = list(map(int,input("enter the marks").split()))
           
enter the marks 21 43 56 768 8776
marks
           
[21, 43, 56, 768, 8776]
marks = tuple(map(int,input("enter the marks").split()))
           
enter the marks 342 546 7565
marks
           
(342, 546, 7565)
marks = set(map(int,input("enter the marks").split()))
           
enter the marks 5243 4326 64753
marks
           
{64753, 5243, 4326}
marks = list(map(float,input("enter the prices").split()))
           
enter the prices 32.23 43.3 23.4
price
           
78.54
prices
           
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    prices
NameError: name 'prices' is not defined. Did you mean: 'price'?
marks = list(map(float,input("enter the price").split()))
           
enter the price 33.4 43.4 
price
           
78.54
del price
           
price
           
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'print'?
marks = list(map(float,input("enter the price").split()))
           
enter the price 34.4 344.4 34.4
price
           
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'print'?
list
           
<class 'list'>
marks
           
[34.4, 344.4, 34.4]
price = tuple(map(float,input("enter the price").split()))
           
enter the price43 43 43
price
           
(43.0, 43.0, 43.0)
price = set(map(float,input("enter the price").split()))
           
enter the price34 43 43
price
           
{34.0, 43.0}
price = set(map(float,input("enter the price").split()))
           
enter the price23 23 23
price
           
{23.0}
a,b=[1,2]
           
a
           
1
b
           
2
a,b,c=(1,12.3,"str")
           
a
           
1
b
           
12.3
c
           
'str'
email,password = input ("enter the email,password:").split()
           
enter the email,password:venkatesulukummara07@gmail.com venkyuv@123
email
           
'venkatesulukummara07@gmail.com'
pass
           
password
           
'venkyuv@123'
name,marks=input("enter the names and marks:").split())
SyntaxError: unmatched ')'
name,marks=input("enter the name and marks:").split())
SyntaxError: unmatched ')'
name,marks=input("enter the name and marks:").split()
enter the name and marks:venky 34
name
'venky'
marks
'34'
int (marks)
34
a,b,c=list (map(int,input().split()))
23 354 564
a
23
b
354
c
564
status = eval(input())
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
status=eval(input())
True
status
True
type(status)
<class 'bool'>
status=eval(input())
2+
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    2+
SyntaxError: invalid syntax
status=eval(input())
2+3j
type(status)
<class 'complex'>
status=eval(input())
[1,2,3,4]
status
[1, 2, 3, 4]
status=eval(input())
(2,3,4,5)
type(status)
<class 'tuple'>
status=eval(input())
{2,3,4,5}
status
{2, 3, 4, 5}
type(status)
<class 'set'>
status=eval(input())
{1:2,2:3,4:5}
type(status)
<class 'dict'>
