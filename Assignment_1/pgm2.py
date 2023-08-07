num = int(input("Enter a number: "))

print("Multiplication Table for {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")