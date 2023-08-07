def all_even_digits(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

even_digit_numbers = [str(num) for num in range(1000, 3001) if all_even_digits(num)]

print(','.join(even_digit_numbers))
