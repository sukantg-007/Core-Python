import mymodule as mm, mymodule1 as mm1, mymodule2 as mm2
#from mymodule import *
print("Addition of 10,20 : ",mm.add(10,20))
print("Addition of 10,20 : ",mm.add(10,20,30))
print("Multiplication of 10,20,30 : ",mm.mult(10,20,30))
print("Multiplication of empty : ",mm.mult())
print("mms pi value : ",mm.pi)
print("REverse of 12345 : ",mm1.reverse(12345))
print("Addition of digit of 12345 : ",mm2.digitadd(12345))