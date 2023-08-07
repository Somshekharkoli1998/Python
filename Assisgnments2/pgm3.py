def generate_square_dict(n):
    square_dict = {}
    for i in range(1, n+1):
        square_dict[i] = i * i
    return square_dict

number = int(input("Enter a number: "))
result_dict = generate_square_dict(number)

print(result_dict)