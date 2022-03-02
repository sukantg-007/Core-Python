'''
list=eval(input("Enter list : "))
print(len(list))
s=eval(input("Enter val : "))
print("count : ",list.count(s))
s1=eval(input("Enter val : "))
if s1 not in list:
    print('Not Available')
else:
    print("Index : ",list.index(s1))
'''
s="Python is easy, python is oop".lower()
print(s)
list=s.split()
print(list)
print(list.count('python'))