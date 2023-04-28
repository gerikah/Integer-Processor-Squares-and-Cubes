>>> INTEGER PROCESSOR: SQUARES AND CUBES

This Python program reads a text file named `integers.txt` that contains 20 integers and creates two separate output text files based on the integers read from the source file. The first output file is named `double.txt` and it contains the square of all even integers found in `integers.txt`. The second output file is named `triple.txt` and it contains the cube of all odd integers found in `integers.txt`.

> Prerequisites

Before running this program, you need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

> How to run the program

1. Clone the repository to your local machine.
2. Open the terminal/command prompt and navigate to the project directory.
3. Make sure that the `integers.txt` file is located in the project directory.
4. Run the following command: ```python number_operations.py```

> Description

This program reads a text file named `integers.txt` that contains 20 integers, and creates two separate output text files based on the integers read from the source file. The first output file is named `double.txt` and it contains the square of all even integers found in `integers.txt`. The second output file is named `triple.txt` and it contains the cube of all odd integers found in `integers.txt`.

> Usage

When the program runs, it reads the `integers.txt` file and processes each integer to calculate its square or cube depending on whether it is even or odd. The program then writes the results to two separate text files: `double.txt` and `triple.txt`.

> Examples

    Example Input

    Suppose the `integers.txt` file contains the following integers:

    ```
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    ```

    Example Output

    After running the program with the above input, two separate text files will be created in the project directory: `double.txt` and `triple.txt`.

    The contents of `double.txt` will be:

    ```
    4
    16
    36
    64
    100
    144
    196
    256
    324
    ```

    The contents of `triple.txt` will be:

    ```
    27
    125
    343
    729
    1331
    2197
    ```

    Note that the even integers in `integers.txt` were squared and written to `double.txt`, and the odd integers were cubed and written to `triple.txt`.

> License

This project is licensed under the MIT License - see the LICENSE.md file for details.

> Acknowledgments

This program was created as part of a Python programming exercise in Object Oriented Programming