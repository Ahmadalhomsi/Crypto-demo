substituted = [5, 10, 15, 20]

result = [item for item in substituted]
print(result)  # [5, 10, 15, 20]


# Binary Conversion

my_array = [10, 5, 23, 12]
binary_array = [bin(num) for num in my_array]
print(binary_array)  # Output: ['0b1010', '0b101', '0b10111', '0b1100']


my_array = [9, 12, 7]
binary_array = [bin(num)[2:] for num in my_array]
print(binary_array)  # Output: ['1001', '1100', '111']
