#reverse of string
'''
this is multiline 
comment
'''
s='abc'
sl=len(s)-1
newstr=''
for i in range(sl,-1,-1):
	newstr=newstr+s[i]

print(newstr)