def binary_to_decimal(binary):
    return int(binary, 2)

input_sequence = input("Enter comma-separated 4-digit binary numbers: ")
binary_numbers = input_sequence.split(',')

divisible_by_5 = [binary for binary in binary_numbers if binary_to_decimal(binary) % 5 == 0]

print(','.join(divisible_by_5))
