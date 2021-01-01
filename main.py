# Very Easy Calculator Library In Python (VECLIP)

# -- Variables --

pi = 3.14159265359

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
        raise ValueError("function 'sqrt' does not accept negative values")
    print(number**0.5)  # Returns a float


def cube(number):
    print(number**3)

# will add cube root

# -- Geometric functions --


def a_cube(side_length):
    print(side_length**2)


def p_cube(side_length):
    print(side_length*4)


def a_triangle(base_length, height):
    print((base_length*height)/2)


def p_triangle(slanted_length, base_length):
    print((slanted_length*2)+base_length)


def a_rectangle(shortside_length, longside_length):
    print(shortside_length * longside_length)


def p_rectangle(shortside_length, longside_length):
    print((shortside_length*2)+(longside_length*2))


def dgnl_square(side_length):
    c = (side_length**2)*2
    print(c**0.5)


def dgnl_rectangle(shortside_length, longside_length):
    a = shortside_length**2
    b = longside_length**2
    c = a + b
    print(c**0.5)


def a_circle(radius):
    print((radius**2)*pi)


def p_circle(radius):
    print((2*pi)*radius)


def sa_cuboid(width, length, height):
    print(2*((width*length)+(width*height)+(height*length)))


def sa_cylinder(radius, height):
    print(2*pi*radius(radius+height))


def v_triangularprism(length, base, height):
    print(length*base*height)


p_circle(5)