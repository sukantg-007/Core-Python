t=tuple([11,22,33,44])
print(t)
print(max(t))
print(min(t))
t1=sorted(t,reverse=True)
print(t1)
t3=tuple(t1)
print(t3)
t3=sorted(t3)
print(t3)
print(type(t3))
print(cmp(t,t1))