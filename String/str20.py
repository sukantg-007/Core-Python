mob=input("Enter ur mobile number : [cc-10digit]")
if mob.startswith("91"):
    print("Ur from India")
elif mob.startswith("86"):
    print("Ur from China")
elif mob.startswith("93"):
    print("Ur from Afgan")
else:
    print("Ur from Refuggie")
    
print("".join(reversed(mob)))

