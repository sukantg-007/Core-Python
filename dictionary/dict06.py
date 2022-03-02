import time as t
dict=eval(input("Enter dictionay : "))
start=t.time_ns()
print(start)
intl=[dict.get(x) for x in dict if type(dict.get(x)) is int]
floatl=[dict.get(x) for x in dict if type(dict.get(x)) is float]
strl=[dict.get(x) for x in dict if type(dict.get(x)) is str]
end=t.time_ns()
print(end)
#floatl=[y for x,y in dict if type(y) is float]
#strl=[y for x,y in dict if type(y) is str]
print('Integer count : ',len(intl))
print('float count : ',len(floatl))
print('String count : ',len(strl))
print('Calculated Time : ',end-start)
#0.0009989