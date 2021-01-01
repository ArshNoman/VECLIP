# Very Easy Calculator Library In Python (VECLIP)

# -- Basic operations --

def add(number1, number2):
    print(number1 + number2)


def substract(number1, number2):
    print(number1 - number2)


def multiply(number1, number2):
    print(number1 * number2)


def divide(number1, number2):
    print(number1 / number2)  # Returns a float

# -- Exponential operations --


def sqr(number):
    print(number * number)

def sqrt(number):
    if number < 0:
        raise ValueError("funtion 'sqrt' does not accept negative values")
    print(number**0.5) # Returns a float

def cube(number):
    print(number**3)

# will add cube root



