Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #mut ord het dyn unidu
>>> d={}
>>> type(d)
<class 'dict'>
>>> d = {1:4,2:8,3:13}
>>> d
{1: 4, 2: 8, 3: 13}
>>> d = {}
>>> d[1]=1
>>> d[12.3]=1
>>> d['str']=1
>>> d[(1,2,4)]=1
>>> d[(2+3j)]=1
>>> d[True]=1
>>> d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d[{2,3,4}]=1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[{2,3,4}]=1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
>>> d[{1:2,3:4}]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[{1:2,3:4}]
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
>>> d[False]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]='str'
>>> d[4]=[1,2,3]
>>> d[5]=(2,3,6)
>>> d[6]=2+6j
d[7]={6,7,8}
d[8]=False
d[9]=frozenset[{4,5,6}]
d[10]={1:2,4:5,8:9}
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (2, 3, 6), 6: (2+6j), 7: {8, 6, 7}, 8: False, 9: frozenset[{4, 5, 6}], 10: {1: 2, 4: 5, 8: 9}, 11: None}
d={}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
data={'name':'dinesh','course':'pfs','batch':'65'}
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65'}
'dinesh' in data
False
65 in data
False
'course' in data
True
data['name']
'dinesh'
data['batch']
'65'
data['age']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('name')
'dinesh'
data.get('batch')
'65'
data.get('age','key is not present')
'key is not present'
data.get('batch','key is not present')
'65'
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65'}
data['age']=21
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65', 'age': 21}
data['phnno']=9876543210
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65', 'age': 21, 'phnno': 9876543210}
data.update({'emai':'venaktesulukummara07@gmail.com','py':2026})
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65', 'age': 21, 'phnno': 9876543210, 'emai': 'venaktesulukummara07@gmail.com', 'py': 2026}
data['age']=22
id(data)
2440781400576
data.popitem()
('py', 2026)
data
{'name': 'dinesh', 'course': 'pfs', 'batch': '65', 'age': 22, 'phnno': 9876543210, 'emai': 'venaktesulukummara07@gmail.com'}
data.pop('course')
'pfs'
data
{'name': 'dinesh', 'batch': '65', 'age': 22, 'phnno': 9876543210, 'emai': 'venaktesulukummara07@gmail.com'}
data.pop('age')
22
data.pop('email')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data.pop('email')
KeyError: 'email'
data.pop('emai')
'venaktesulukummara07@gmail.com'
data
{'name': 'dinesh', 'batch': '65', 'phnno': 9876543210}
del data['batch']
data
{'name': 'dinesh', 'phnno': 9876543210}
data.clear()
data
{}
data=({'name': 'dinesh', 'batch': '65', 'phnno': 9876543210})
len(data)
3
data.keys()
dict_keys(['name', 'batch', 'phnno'])
data.values()
dict_values(['dinesh', '65', 9876543210])
data.items()
dict_items([('name', 'dinesh'), ('batch', '65'), ('phnno', 9876543210)])
stored(data)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    stored(data)
NameError: name 'stored' is not defined. Did you mean: 'sorted'?
sorted(data)
['batch', 'name', 'phnno']
max(data)
'phnno'
min(data)
'batch'
d={1:1,2:2}
m = d
m[3]=3
m
{1: 1, 2: 2, 3: 3}
d
{1: 1, 2: 2, 3: 3}
n=d.copy()
n[5]=5
n
{1: 1, 2: 2, 3: 3, 5: 5}
d
{1: 1, 2: 2, 3: 3}
data
{'name': 'dinesh', 'batch': '65', 'phnno': 9876543210}
#if we use set default if the key is not present in the dict it gonna upadate
data.setdefault('name',2026)
'dinesh'
data.setdefault('age',2026)
2026
data.setdefault('key',2026)
2026
data
{'name': 'dinesh', 'batch': '65', 'phnno': 9876543210, 'age': 2026, 'key': 2026}
data.setdefault('emai',2026)
2026
dict.fromkeys(["python","mysql","java"],0)
{'python': 0, 'mysql': 0, 'java': 0}
