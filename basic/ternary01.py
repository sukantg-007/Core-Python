# true if condition else false
#input(message in string): string
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))

# if a>b:
#     max=a
# else:
#     max=b
# print(max)
# print(type(a))
max=a if a>b and a>c else b if b>c else c
print("Maximum value : ",max)