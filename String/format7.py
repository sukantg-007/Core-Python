dict={"name":"AAA","addr":"Daund"}
print(dict)
print("Ur name : ",dict.get("name"))
print("Ur Addr : ",dict.get("addr"))
print("Ur name : ",dict.get("name"),"Ur Addr : ",dict.get("addr"))
print("Ur name : {d[name]} Ur Addr : {d[addr]}".format(d=dict))
print("Ur name : {name} Ur Addr : {addr}".format(**dict))