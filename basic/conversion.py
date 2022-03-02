'''
printf("Enter a number : ");
scanf("%d",&variable);
'''
val1=input("Enter a numnber : ")
val2=input("Enter a numnber : ")
printf(val1+val2)

Func-name	|Allowed Values																|Converted Value
--------------------------------------------------------------------------------------------------------
int()		|int, float, boolean, str(only that string whoes base is 10-integer value)	|int
float()		|int,float,bool, str(both string whoes base is 10-integer and float value)	|float
complex(x)	|int,float,complex,bool,str(both string whoes base is 10-integer and float)	|complex
complex(x,y)|																			|
bool()		|int,float,complex,bool,str													|boolean
str()		|int,float,complex,bool,str													|string

x=4+5j
x.read
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.read
AttributeError: 'complex' object has no attribute 'read'. Did you mean: 'real'?
x.real
4.0
x.imag
5.0
OB1111+5J
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    OB1111+5J
NameError: name 'OB1111' is not defined
0B1111+5j
(15+5j)
0b1111+0x123j
SyntaxError: invalid hexadecimal literal
s='abc'
s[0]
'a'
len(s)
3
s[0:2]
'ab'
s[:2]
'ab'

s[1:]
'bc'
s[:]
'abc'
s[-1]
'c'
s[-2]
'b'
s[-1:-3]
''
s[-3:-1]
'ab'
s[::-1]
'cba'
int(10)
10
int(10.5)
10
int(4+5j)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(4+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
int('10')
10
int('10.5')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int('10.5')
ValueError: invalid literal for int() with base 10: '10.5'
int('ab10')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('ab10')
ValueError: invalid literal for int() with base 10: 'ab10'
float(10)
10.0
float(10.5)
10.5
float(4+5j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float('10')
10.0
float('10.5')
10.5
complex(10)
(10+0j)
complex(10.5)
(10.5+0j)
complex(10,10.5)
(10+10.5j)
complex(4+5j)
(4+5j)
complext(True)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complext(True)
NameError: name 'complext' is not defined. Did you mean: 'complex'?
complex(True)
(1+0j)
complex('10')
(10+0j)
complex('10.5')
(10.5+0j)
complex('ab10')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex('ab10')
ValueError: complex() arg is a malformed string
bool(10)
True
bool(-10)
True
bool(0)
False
bool(10.5)
True
bool(4+5j)
True
bool(4+0j)
True
bool(0+0j)
False
bool(0+4j)
True
bool(True)
True
bool('10')
True
bool('abc10')
True
bool('')
False
str(10)
'10'
str(10.5_
    
SyntaxError: invalid decimal literal
str(10.5)
    
'10.5'
\
str(True)
    
'True'
str('abc')
    
'abc'
