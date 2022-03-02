list=[10,20,30]
t=tuple(list)
t
(10, 20, 30)
type(t)
<class 'tuple'>
r=range(1,4)
t
(10, 20, 30)
r
range(1, 4)
type(r)
<class 'range'>
for i in r:
    print(i)

1
2
3
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(3,10):
    print(i)

    
3
4
5
6
7
8
9
for i in range(0,10,2):
    print(i)

    
0
2
4
6
8
for i in range(1,10,2):
    print(i)

    
1
3
5
7
9
for i in range(0,10,4):
    print(i)

    
0
4
8
list=[1,2,3,4,5,6,7,8]
for i in range(len(list)):
    print(list[i])

    
1
2
3
4
5
6
7
8
r=range(1,4)
for i in r:
    print(i)

    
1
2
3
r[0]=11
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    r[0]=11
TypeError: 'range' object does not support item assignment
s={}
type(s)
<class 'dict'>
s={1,2,4}
type(s)
<class 'set'>
list=[1,2,3,4,1,3]
list
[1, 2, 3, 4, 1, 3]
s=set(list)
s
{1, 2, 3, 4}
list=[7,2,6,3,1]
list
[7, 2, 6, 3, 1]
s=set(list)
s
{1, 2, 3, 6, 7}
s.remove(3)
s
{1, 2, 6, 7}
s.add(0)
s
{0, 1, 2, 6, 7}
fs=frozenset(s)
type(fs)
<class 'frozenset'>
fs
frozenset({0, 1, 2, 6, 7})
fs.remove(2)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fs.remove(2)
AttributeError: 'frozenset' object has no attribute 'remove'
fs.add(5)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    fs.add(5)
AttributeError: 'frozenset' object has no attribute 'add'
fs=frozenset(list)
type(fs)
<class 'frozenset'>
fs
frozenset({1, 2, 3, 6, 7})
d={}
type(d)
<class 'dict'>
d[1]="Python"
d
{1: 'Python'}
d[1]="Java"
d
{1: 'Java'}
d['a']="Python"
d
{1: 'Java', 'a': 'Python'}
d[1]
'Java'
for i in d.keys():
    print(i)

    
1
a
for i in d.keys():
    print(d[i])

    
Java
Python
list=d.keys()
list
dict_keys([1, 'a'])
values_list=d.values()
values_list
dict_values(['Java', 'Python'])
for i in d.items():
    print(i)

    
(1, 'Java')
('a', 'Python')
