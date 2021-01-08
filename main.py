# Very Easy Calculator Library In Python (VECLIP)

from statistics import mode as m
import math

# -- Variables --

pi = 3.14159265359
phi = 1.618033988749895
eulars_number = 2.71828
wallis_constant = 2.094551481542326

# -- Basic operations -- 4


def add(number1, number2):
    if isinstance(number1 or number2, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number1 + number1)

def subtract(number1, number2):
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
    print(number1 / number2)

# -- Exponential operations -- 5

def power(base, exponent):
    if isinstance(base or exponent, str):
        raise ValueError("strings cannot be taken as a parameter")
    is_negative = False
    b = base
    if exponent == 0:
        print(1)
    if exponent < 0:
        is_negative = True
        for x in range(1, abs(exponent)):
            b = b*base
    else:
        for x in range(1, exponent):
            b = b*base
    if not is_negative:
        print(b)
    else:
        print(f"1/{b}")

def sqr(number):
    if isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number * number)

def sqrt(number):
    if number < 0:
        raise ValueError("function 'sqrt' does not accept negative values")
    elif isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number**0.5)  # Returns a float

def cube(number):
    if isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number**3)

def cubert(number):
    if number < 0:
        raise ValueError("function 'sqrt' does not accept negative values")
    elif isinstance(number, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(number ** (1. / 3))

# -- Geometric functions -- 17


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
    print(((side_length**2)*2)**0.5)

def dgnl_rectangle(shortside_length, longside_length):
    if isinstance(shortside_length or longside_length, str):
        raise ValueError("strings cannot be taken as a parameter")
    print(((shortside_length**2)+(longside_length**2))**0.5)

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

# -- Trigonometry Functions -- 9

def exterior_angle(i_angle1, i_angle2):
    if i_angle2 < 0 or i_angle1 < 0:
        raise ValueError("function 'exterior_angle' does not accept negative values")
    elif isinstance(i_angle1 or i_angle2, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif (i_angle1 + i_angle2) > 180:
        raise ValueError("the total value is larger than 180 degrees")
    print(i_angle2+i_angle1)

def pythagorean(a, b):
    sqrt((a*a)+(b*b))

def reverse_pythagorean(hypotenuse, x):
    sqrt((hypotenuse*hypotenuse)-(x*x))

def deg_sin(x):
    print(math.sin(math.radians(x)))

def deg_cos(x):
    print(math.cos(math.radians(x)))

def deg_tan(x):
    print(math.tan(math.radians(x)))

def rad_sin(x):
    print(math.sin(x))

def rad_cos(x):
    print(math.cos(x))

def rad_tan(x):
    print(math.tan(x))

# -- Statistics -- 4

def mean(*args):
    mean_list = list(args)
    for term in mean_list:
        if isinstance(term, str):
            raise ValueError("strings cannot be taken as a parameter")
    print(sum(mean_list)/len(mean_list))

def mode(*args):
    x = list(args)
    for term in x:
        if isinstance(term, str):
            raise ValueError("strings cannot be taken as a parameter")
    print(m(x))

def range(*args):
    x = list(args)
    for term in x:
        if isinstance(term, str):
            raise ValueError("strings cannot be taken as a parameter")
    x.sort()
    print(x[-1] - x[0])

def median(*args):
    x = list(args)
    for term in x:
        if isinstance(term, str):
            raise ValueError("strings cannot be taken as a parameter")
    x.sort()
    print(x)
    if len(x) % 2 == 0:
        print((x[int(len(x)/2)]+x[int(len(x)/2)-1])/2)
    else:
        print(x[int(len(x)/2)])

# -- Electricity -- 4

def volts(watts=0, amperes=0, ohms=0):
    if isinstance(watts or amperes or ohms, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif watts and amperes and ohms != 0:
        raise ValueError("please fill only 2 out of 3 parameters")
    if watts and amperes != 0:
        print(watts/amperes)
    elif watts and ohms != 0:
        print((watts*ohms)**0.5)
    elif ohms and amperes != 0:
        print(amperes*ohms)
    else:
        raise ValueError("please provide the proper number parameters")

def ohms(watts=0, amperes=0, volts=0):
    if isinstance(watts or amperes or volts, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif watts and amperes and volts != 0:
        raise ValueError("please fill only 2 out of 3 parameters")
    if watts and amperes != 0:
        print(watts/(amperes*amperes))
    elif watts and volts != 0:
        print((volts*volts)/watts)
    elif volts and amperes != 0:
        print(volts/amperes)
    else:
        raise ValueError("please provide the proper number of parameters")

def watts(ohms=0, amperes=0, volts=0):
    if isinstance(ohms or amperes or volts, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif ohms and amperes and volts != 0:
        raise ValueError("please fill only 2 out of 3 parameters")
    if ohms and amperes != 0:
        print(ohms/(amperes*amperes))
    elif ohms and volts != 0:
        print((volts*volts)/ohms)
    elif volts and amperes != 0:
        print(volts*amperes)
    else:
        raise ValueError("please provide the proper number of parameters")

def amperes(ohms=0, watts=0, volts=0):
    if isinstance(ohms or watts or volts, str):
        raise ValueError("strings cannot be taken as a parameter")
    elif ohms and watts and volts != 0:
        raise ValueError("please fill only 2 out of 3 parameters")
    if ohms and watts != 0:
        print((watts/ohms)**0.5)
    elif ohms and volts != 0:
        print(volts/ohms)
    elif volts and watts != 0:
        print(watts/volts)
    else:
        raise ValueError("please provide the proper number of parameters")

# -- Algebra -- 1

def add_exp(base1, exp1, base2, exp2):
    banned_list = ['0','1','2','3','4','5','6','7','8','9']
    if isinstance(base1 or base2, int or float):
        raise ValueError("parameters base1 and base2 cannot be numbers")
    if isinstance(exp1 or exp2, str):
        raise ValueError("parameters exp1 and exp2 cannot be numbers")
    for bad in banned_list:
        if base1 == bad or base2 == bad:
            raise ValueError("parameters base1 and base2 cannot be numbers")
    if base2 != base1:
        print(base1, exp1, base2, exp2)
    else:
        print(base1, (exp1*exp2))

def substract_exp(base1, exp1, base2, exp2):
    banned_list = ['0','1','2','3','4','5','6','7','8','9']
    if isinstance(base1 or base2, int or float):
        raise ValueError("parameters base1 and base2 cannot be numbers")
    if isinstance(exp1 or exp2, str):
        raise ValueError("parameters exp1 and exp2 cannot be numbers")
    for bad in banned_list:
        if base1 == bad or base2 == bad:
            raise ValueError("parameters base1 and base2 cannot be numbers")
    if base2 != base1:
        print(base1, exp1, base2, exp2)
    new_exp = exp1 - exp2
    if new_exp > 0:
        print(base1, (exp1-exp2))
    elif new_exp < 0:
        print(f"1/{base1}{exp1 - exp2}")
    else:
        print(1)

def multiply_exp(base1, exp1, base2, exp2):
    banned_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if isinstance(base1 or base2, int or float):
        raise ValueError("parameters base1 and base2 cannot be numbers")
    if isinstance(exp1 or exp2, str):
        raise ValueError("parameters exp1 and exp2 cannot be numbers")
    for bad in banned_list:
        if base1 == bad or base2 == bad:
            raise ValueError("parameters base1 and base2 cannot be numbers")
    if base2 != base1:
        print(base1, exp1, base2, exp2)
    else:
        print(base1, (exp1 + exp2))

#  46 functions
