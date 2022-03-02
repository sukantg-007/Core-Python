dict=eval(input("Enter dictionay : "))
sum=0
for k in dict:
    v=dict.get(k)
    if type(v) is int or type(v) is float:
        sum+=v
print('Sum of values : ',sum)
