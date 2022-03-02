#string is immutable
#it will create one object having same content
s='python'
s1="python 1"
s2='''python 2'''

print(s)
print(s1)
print(s2)
print(id(s))
print(id(s1))
print(id(s2))