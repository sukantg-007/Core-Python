float="{:{align}{width}{precision}}"
print(float.format(123.25,align="^",width=6,precision=3))
print(float.format(123.25,align="<",width=6,precision=3))
print(float.format(123.25,align=">",width=6,precision=3))
print(float.format(123.25,align="^",width=1,precision=3))