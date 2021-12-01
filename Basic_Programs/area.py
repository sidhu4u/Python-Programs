def circle_area():
    radius = float(input("Enter the Radius value : "))
    area = 3.14 * (radius ** 2)
    return f"Area of Circle = {area}"


def rectangle_area():
    base = float(input("Enter Base value : "))
    height = float(input("Enter Height value : "))
    area = base * height
    return f"Area of Rectangle = {area}"


def triangle_area():
    base = float(input("Enter Base value : "))
    height = float(input("Enter Height value : "))
    area = (base * height)/2
    return f"Area of Triangle = {area}"


def square_area():
    side = float(input("Enter the side value : "))
    area = side ** 2
    return f"Area of Square = {area}"


def rhombus_area():
    length = float(input("Enter Length value : "))
    height = float(input("Enter Height value : "))
    area = (length * height) / 2
    return f"Area of Rhombus = {area}"


def default():
    return "Incorrect Choice. try again"


switching = {

    '1': circle_area,
    '2': rectangle_area,
    '3': triangle_area,
    '4': square_area,
    '5': rhombus_area
}


def go(ch):
    return switching.get(ch, default)()
