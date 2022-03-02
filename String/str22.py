s=input("Enter a single letter : ")
if s.isalnum():
    print("Alpha-numeric character")
    if s.isalpha():
        print('Alphabate')
        if s.islower():
            print("Case : Lowercase")
        elif s.isupper():
            print("Case : Uppercase")
    elif s.isdigit():
        print("Number")
elif s.isspace():
    print("Its a space")
    
