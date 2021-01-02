# Very Easy Calculator Library In Python (VECLIP)

# -- Variables --

pi = 3.14159265359

# -- Basic operations --


def add(number1, number2):
    if isinstance(number1 or number2, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number1 + number2)

def substract(number1, number2):
    if isinstance(number1 or number2, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number1 - number2)

def multiply(number1, number2):
    if isinstance(number1 or number2, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number1 * number2)

def divide(number1, number2):
    if isinstance(number1 or number2, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number1 / number2)  # Returns a float

# -- Exponential operations --

def power(base, exponent):
    if isinstance(base or exponent, str):
        raise ValueError("strings cannot be taken as a parameter")
    b = base
    for x in range(1, exponent):
        base = b*base

def sqr(number):
    if isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number * number)

def sqrt(number):
    if number < 0:
        raise ValueError("function 'sqrt' does not accept negative values")
    print(number**0.5)  # Returns a float

def cube(number):
    if isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number**3)

# will add cube root

# -- Geometric functions --


def a_square(side_length):
    if isinstance(side_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(side_length**2)

def p_square(side_length):
    if isinstance(side_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(side_length*4)

def a_triangle(base_length, height):
    if isinstance(base_length or height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print((base_length*height)/2)

def p_triangle(slanted_length, base_length):
    if isinstance(base_length or slanted_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print((slanted_length*2)+base_length)

def a_rectangle(shortside_length, longside_length):
    if isinstance(shortside_length or longside_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(shortside_length * longside_length)

def p_rectangle(shortside_length, longside_length):
    if isinstance(shortside_length or longside_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print((shortside_length*2)+(longside_length*2))

def dgnl_square(side_length):
    if isinstance(side_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    c = (side_length**2)*2
    print(c**0.5)

def dgnl_rectangle(shortside_length, longside_length):
    if isinstance(shortside_length or longside_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    a = shortside_length**2
    b = longside_length**2
    c = a + b
    print(c**0.5)

def a_circle(radius):
    if isinstance(radius, str):
        raise ValueError("strings cannot be taken as a parameter")
    print((radius**2)*pi)

def c_circle(radius):
    if isinstance(radius, str):
        raise ValueError("strings cannot be taken as a parameter")
    print((2*pi)*radius)

def v_sphere(radius):
    if isinstance(radius, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(4/3*pi*(radius*radius*radius))

def sa_circle(radius):
    if isinstance(radius, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(4*pi*(radius*radius))

def sa_cuboid(width, length, height):
    if isinstance(length or width or height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(2*((width*length)+(width*height)+(height*length)))

def sa_cylinder(radius, height):
    if isinstance(radius or height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(2*pi*radius(radius+height))

def sa_rightcylindrical_triangle(circumference, slanted_height):
    if isinstance(circumference or slanted_height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(1/2*circumference*slanted_height)

def v_rightcylindrical_cone(radius, height):
    if isinstance(radius or height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(1/3*pi*(radius**2)*height)

def v_triangularprism(length, base, height):
    if isinstance(length or base or height, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(length*base*height)

#  25 functions
