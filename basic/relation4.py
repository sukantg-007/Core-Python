per=int(input("Enter ur Percentage : "))
if per>75:
	print('Distinction with first class')
elif per>60 and per <=75:
	print('First Class')
elif not(per>=35 and per <=60):
	print('Pass class')
else:
	print('Try next time')