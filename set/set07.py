#set comprehension
s={x for x in range(1,11)}
print(s)
s={pow(x,2) for x in range(1,11)}
print(s)
s={x for x in range(1,11) if x%2!=0}
print(s)
s={(x,x**2,x**3) for x in range(1,11)}
print(s)
#s={{1,2},{3,4},{5,6}}
#print(s)
s1={z for (x,y,z) in s}
print(s1)