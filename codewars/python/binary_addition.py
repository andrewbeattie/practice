"""
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.
The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


https://peps.python.org/pep-0498/

"""

def add_binary_1(a, b):
    binary = f"{a+b:08b}"
    return binary.lstrip("0")

def add_binary_2(a, b):
    a, b = bin(a), bin(b)
    return a[2:] + b[2:]

def add_binary_3(a, b):
    return bin(a+b)[2:]