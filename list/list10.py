x=[1,2,3,4]
y=x
y[2]=22
print(x)
print(y)
if x is y:
    print("Both point to same obj")
else:
    print("Not")