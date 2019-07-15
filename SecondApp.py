# logical constructions

a = input("Enter first number ")
b = input("Enter second number ")

if int(a) > int(b):
    print("{a} > {b}", a, b)
elif int(a) < int(b):
    print("{a} < {b}",a,b)
else:
    print("{a} = {b}",a,b)