Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operators
#arithmatic operators
a=10
b=5
a+b
15
a-b
5
a*b
50
a/2
5.0
b/2
2.5
a//2
5
b//2
2
9/2
4.5
16/3
5.333333333333333
16//3
5
a%2
0
17/2
8.5
17%2
1
17//2
8
a>b
True
a<=b
False
a>=b
True
a>=10
True
a==b
False
a!=b
True
#assingnment operators
a=20
a=a
a=a
a=20
a=a+10
a
30
a=a+20
a
50
a +=10
a
60
a -=10
a *=20
a
1000
a //= 2
a
500
a **=2
a
250000
a /=500
a
500.0
#Relational operators
#Relational operators

a=15
email = true
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    email = true
NameError: name 'true' is not defined. Did you mean: 'True'?
email = True
password = False
email and password
False
login  = True
login = False
display_products = True
'a' is 'aeiou'
False
'a' is not 'aeiou'
True
7%2== and 3%2==0
SyntaxError: invalid syntax
7%2==0 and 3%2==0
False
9%2==0 and 18%2==0
False
18%2==0
True
not 9%2 ==0
True

#membership operators
'python' in s
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    'python' in s
NameError: name 's' is not defined
#membership operators
#str list tuple set dict
s = 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'a' in s
True
'p' in s
True
l =[1,2,3,4]
'10' in l
False
'4' in l
False
'2' in l
False
2 in l
True
4 in l
True
t = (20,40,60)
40 in t
True
50 in t
False
25 in t
False
s = {pen,paper,book,bus}
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s = {pen,paper,book,bus}
NameError: name 'pen' is not defined. Did you mean: 'len'?
s = {'pen','paper','book','bus'}
pen in s
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    pen in s
NameError: name 'pen' is not defined. Did you mean: 'len'?
'pen' in s
True
'paper' in s
True
'chocalate' in s
False

#identity operators
#identity operators
l = [1,2,3,4]
m = [1,2,3,4]
>>> id (l)
1906820992704
>>> id (m)
1906820990016
>>> l == m
True
>>> l is m
False
>>> m is l
False
>>> n = m
>>> n
[1, 2, 3, 4]
>>> id (n)
1906820990016
>>> m is n
True
>>> n is l
False
>>> n is not l
True
>>> 
>>> #bitwise operators
>>> 
>>> 11 & 12
8
>>> 11
11
|
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> 2<<2
8
>>> 16>>3
2
>>> ~ 17
-18
>>> ~20
-21
