def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


print(fact(5))

def reverse(n):
    if n<10:
        return n
    else:
        
        return str(str(n%10)+str(reverse(n//10)))

print(reverse(557))

# Reverse a number using recursion

def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10 + n%10)


reversed_number = reverse(123,0)

# Display output
print("Reverse of %d is %d" %(123, reversed_number))