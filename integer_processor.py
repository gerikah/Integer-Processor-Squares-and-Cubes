# Open the input file 'integers.txt' in read mode
with open ("integers.txt", "r") as num_file:

# Read the integers from the file and store them in a list
    integers = num_file.read().splitlines
    
# Create two empty lists, even_integers and odd_integers
even_integers = []
odd_integers = []

# Loop through the list of integers:
for num in integers:
    
    # If the integer is even, append it to even_integers list
    if num % 2 == 0:
        even_integers.append(num)
    # If the integer is odd, append it to odd_integers list
    else:
        odd_integers.append(num)

# Create two empty lists, squares and cubes
square_even_integers = []
cube_odd_integers = []

# Loop through the even_integers list:
for num in even_integers:
    # Calculate the square of each integer and append it to squares list
    square = num ** 2
    square_even_integers.append(square)

# Loop through the odd_integers list:
for num in odd_integers:
    # Calculate the cube of each integer and append it to cubes list
    cube = num ** 3
    cube_odd_integers.append(cube)

# Open the first output file 'double.txt' in write mode
with open ("double.txt", "w") as num_file:

# Loop through the squares list:
    # Write each square to the file followed by a new line character
# Close the first output file
# Open the second output file 'triple.txt' in write mode
with open ("triple.txt", "w") as num_file:
     
# Loop through the cubes list:
    # Write each cube to the file followed by a new line character
# Close the second output file