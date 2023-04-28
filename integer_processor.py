# open the input file 'integers.txt' in read mode
with open('integers.txt', 'r') as num_file:
    # read the integers from the file and store them in a list
    integers = num_file.read().splitlines()

# convert the list of strings to a list of integers
integers = list(map(int, integers))

# create two empty lists, even_integers and odd_integers
even_integers = []
odd_integers = []

# loop through the list of integers and append even and odd integers to their respective lists
for num in integers:
    if num % 2 == 0:
        even_integers.append(num)
    else:
        odd_integers.append(num)

# create two empty lists, squares and cubes
squares_even_integers = []
cubes_odd_integers = []

# loop through the even_integers list and calculate the square of each integer
for num in even_integers:
    # calculate the square of each integer and append it to squares list
    square = num ** 2
    squares_even_integers.append(square)

# loop through the odd_integers list and calculate the cube of each integer
for num in odd_integers:
    # calculate the cube of each integer and append it to cubes list
    cube = num ** 3
    cubes_odd_integers.append(cube)

# open the first output file 'double.txt' in write mode
with open('double.txt', 'w') as num_file:
    # loop through the squares list and write each square to the file followed by a new line character
    for square in squares_even_integers:
        num_file.write(str(square) + '\n')

# close the first output file
num_file.close()

# open the second output file 'triple.txt' in write mode
with open('triple.txt', 'w') as num_file:
    # loop through the cubes list and write each cube to the file followed by a new line character
    for cube in cubes_odd_integers:
        num_file.write(str(cube) + '\n')

# close the second output file
num_file.close()
