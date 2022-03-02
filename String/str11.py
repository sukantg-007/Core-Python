#removing spaces
s=input("Enter user-name : ")
#s=s.lstrip()---it remove spaces from left side
#s=s.rstrip()---it remove spaces from right side
#strip()----it remove spaces from left and right both side
s=s.strip()
if s=='admin':
    print("Correct User-name")
else:
    print("Not-Correct User-name")
