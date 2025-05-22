import math

def main():
    shape = input("Enter shape (circle/rectangle): ")
    if shape == "circle":
        r = float(input("Enter radius: "))
        area = math.pi * r * r
        print("Area of the circle is:", area)
    elif shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
        print("Area of the rectangle is:", area)
    else:
        print("Invalid shape")

main()