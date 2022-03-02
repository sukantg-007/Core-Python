#object cloening
#first way using slice operator
print("---------------using slice op---------------")
x=[1,2,3,4,5]
y=x[:]
print(x)
print(y)
y[2]=22
print(x)
print(y)
if x is y:
    print("Both pointing to single obj")
else:
    print("Both pointing to seperate obj")

print("---------------using copy()---------------")
#another way: using copy() function
x=[1,2,3,4,5]
y=x.copy()
print(x)
print(y)
y[2]=22
print(x)
print(y)
if x is y:
    print("Both pointing to single obj")
else:
    print("Both pointing to seperate obj")