b=10
type(b)
<class 'int'>
b=3.14
type(b)
<class 'float'>
b=True
type(b)
<class 'bool'>
b=4+3i
SyntaxError: invalid decimal literal
b=3+4j
type(b)
<class 'complex'>
b='A'
type(b)
<class 'str'>
b=0B1111
b
15
b=0O123
b
83
b=0xface
b
64206
b=0X60
b
96
b=0o158
SyntaxError: invalid digit '8' in octal literal
bin(15)
'0b1111'
oct(83)
'0o123'
hex(96)
'0x60'
