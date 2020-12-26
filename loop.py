magicians = ['as', 'bb', 'cc']

for magician in magicians:
    print(magician)

for value in range(1, 5):
    print(value)

print(list(range(1, 5)))

squares = [value ** 2 for value in range(1, 11)]
print("squares", squares)

print(squares[0:3], squares[-3:])

newSquares = squares[:];

print('newSquares', newSquares)