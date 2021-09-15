A = input('Getal A: ')
B = input('Getal B: ')

if A > B:
    Max = A
    Min = B
    print('A is het grootste getal: ' + Max)
    print('Maximum: ' + Max)
    print('Minimum: ' + Min)
elif A < B:
    Min = A
    Max = B
    print('B is het kleinste getal: ' + Min)
    print('Maximum: ' + Max)
    print('Minimum: ' + Min)
else:
    print('A en B zijn even groot')
    print('Maximum: ' + A)
    print('Minimum: ' + B)