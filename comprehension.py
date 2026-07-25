squares = [ x ** 2 for x in range(1, 6)]
print(squares)

even_squares = []

for x in range(1, 11):
    if x % 2 == 0:
        even_squares.append(x ** 2)

even_squares = [ x ** 2 for x in range(1, 11) if x % 2 == 0 ]

print(even_squares)

