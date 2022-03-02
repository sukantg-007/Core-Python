a=10
b=10
id(a)
2150342328848
id(b)
2150342328848
a=30
id(a)
2150342329488
id(b)
2150342328848
b=None
id(b)
140728100423672
type(b)
<class 'NoneType'>
b=bytes(10,20)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b=bytes(10,20)
TypeError: bytes() argument 'encoding' must be str, not int
b=bytes([10,20])
type(b)
<class 'bytes'>
b=bytes([255,250])
types(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    types(b)
NameError: name 'types' is not defined. Did you mean: 'type'?
type(b)
<class 'bytes'>
b=bytes([256,255])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b=bytes([256,255])
ValueError: bytes must be in range(0, 256)
b[0]
255
b[1]
250
b[2]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b[2]
IndexError: index out of range
b[:]
b'\xff\xfa'
b[1:]
b'\xfa'
b[0]=110
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b[0]=110
TypeError: 'bytes' object does not support item assignment
b=byte([10,20,30])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b=byte([10,20,30])
NameError: name 'byte' is not defined. Did you mean: 'bytes'?
b=bytes([10,20,30])
b
b'\n\x14\x1e'
b=bytearray([10,20,30])
type(b)
<class 'bytearray'>
b[0]
10
b[0]=11
b[0]
11
for i in b:
    print(i)

11
20
30
list=[1,3,4]
type(list)
<class 'list'>
list[0]=11
list.append(12)
for i in list:
    print(i)

11
3
4
12
list
[11, 3, 4, 12]
list.remove(4)
list
[11, 3, 12]
len(list)
3
list.append('Python')
list
[11, 3, 12, 'Python']
list[0]=33
list
[33, 3, 12, 'Python']
list[:]
[33, 3, 12, 'Python']
list[1:]
[3, 12, 'Python']
list[::-1]
['Python', 12, 3, 33]
list
[33, 3, 12, 'Python']
len(list)
4
for i in range(len(list)):
    print(list[i])

33
3
12
Python
tuple=()
type(tuple)
<class 'tuple'>
tuple.append(10)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    tuple.append(10)
AttributeError: 'tuple' object has no attribute 'append'
tuple[0]=1
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tuple[0]=1
TypeError: 'tuple' object does not support item assignment
t=tuple([10,20,30])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t=tuple([10,20,30])
TypeError: 'tuple' object is not callable
t=(10,20,30)
type(t)
<class 'tuple'>
t
(10, 20, 30)
t=tuple(list)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t=tuple(list)
TypeError: 'tuple' object is not callable
list
[33, 3, 12, 'Python']
t=(list)
t
[33, 3, 12, 'Python']
type(t)
<class 'list'>
simple_list=list
t=tuple(simple_list)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    t=tuple(simple_list)
TypeError: 'tuple' object is not callable
list
[33, 3, 12, 'Python']
t=tuple(i for i in list)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t=tuple(i for i in list)
TypeError: 'tuple' object is not callable
list.remove('Python')
list
[33, 3, 12]
t=tuple(list)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    t=tuple(list)
TypeError: 'tuple' object is not callable
