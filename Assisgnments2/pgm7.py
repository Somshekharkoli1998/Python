def generate_2d_array(X, Y):
    array = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        array.append(row)
    return array

input_str = input("Enter two digits (X,Y) separated by a comma: ")
X, Y = map(int, input_str.split(','))

result_array = generate_2d_array(X, Y)

for row in result_array:
    print(row)
