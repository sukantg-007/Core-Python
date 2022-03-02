# a,b,c=[int(x) for x in input("Enter 3 nos : ").split()]
# print('a : ',a)
# print('b : ',b)
# print('c : ',c)
# print(a+b+c)

# a,b,c=[int(x) for x in input("Enter 3 nos : ").split(",")]
# print('a : ',a)
# print('b : ',b)
# print('c : ',c)
# print(a+b+c)

# a,b,c=[int(x) for x in input("Enter 3 nos : ").split(":")]
# print('a : ',a)
# print('b : ',b)
# print('c : ',c)
# print(a+b+c)

a,b,c=[eval(x) for x in input("Enter 3 nos : ").split("#")]
print('a : ',a)
print('b : ',b)
print('c : ',c)
print(a+b+c)