import time as t
statt=t.time_ns()
for i in range(100000000):
    pass
endt=t.time_ns()
print((endt-statt)/10**9)