number = input("Enter long integer: ")
num_zero = 0
for char in number:
    if char=='0':
        num_zero += 1
print(num_zero)
