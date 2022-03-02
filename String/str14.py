dict={"india":91,"china":86,"pak":92,"afghan":93}
country=input("enter your country : ")
mob=input("enter your mobile number : ")
ext=""
for i in dict.keys():
    if country==i:
        ext=dict.get(i)
mob=str(ext)+"-"+mob
print("ur mobile number : ",mob)