print(10+5) #additon:15
print(10-5) #substraction: 5
print(10*5) #multiplication: 50
print(10%3) #modulus: 1
print(2**3) #Exponentiation : 8
print(10//3) #Output: 3

a = 10
b = 20
print(a==b) #Output: False
print(a!=b) #Output: True
print(a>b)  #Output: False
print(a < b) # Output: True
print(a >= b) #Output: False
print(a<=b) #Output : True

a = 10
b = 20
c = a

print(a is b) # False
print(a is c) # True
print(a is not b) #True

x = 24
y = 20
lst = [10, 20, 30, 40, 50]
print(x in lst) # False
print(y in lst) # True
print(x not in lst) # True

#bitwise operators
a = 10 # 1010 in binary
b = 4  # 0100 in binary
print(a&b) #output: 0 (0000 in binary)
print(a|b) # output: 14(1110 in binary)
print(~a) # output: -11(inverts all bits)
print(a^b) #output: 14 (1110 in binary)
print(a >> 2) #output: 2 (0010 in binary)
print(a << 2) # output 40 (101000 in binary)

print(100+ 5*3) #output: 115