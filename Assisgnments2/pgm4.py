input_string = input("Enter comma-separated numbers: ")
numbers_list = input_string.split(',')
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)