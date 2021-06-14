#Created by Christian Mascunana 06/14/2021
import math

class Shape:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def CheckForFloat():
    while True:
        try:
            x = float(input("User=> "))
            break
        except ValueError:
            print ("Error: Entry was not a number")
    return x

def AreaMath():
    while True:
        print ("\nArea")
        print ("Enter 'S' for Square, 'R' for Rectangle, 'T' for Triangle,\n'RT' for Right Triangle or 'C' for Circle")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='S'): #for squares a is the side length
            print ("\nPlease input the side length")
            shape.a = CheckForFloat()
            area = shape.a**2
            shapename = "Square"
            break
        elif (x=='R'): #for rectangles a is length b is width
            print ("\nPlease input the length")
            shape.a = CheckForFloat()
            print ("\nPlease input the width")
            shape.b = CheckForFloat()
            area = shape.a*shape.b
            shapename = "Rectangle"
            break
        elif (x=='RT'): #for right triangle a is base and b is height
            print ("\nPlease input the base")
            shape.a = CheckForFloat()
            print ("\nPlease input the height")
            shape.b = CheckForFloat()
            area = 0.5*shape.a*shape.b
            shapename = "Right Triangle"
            break
        elif (x=='T'):
            print ("\nPlease input side A length")
            shape.a=CheckForFloat()
            print ("\nPlease input side B length")
            shape.b=CheckForFloat()
            print ("\nPlease input side C length")
            shape.c=CheckForFloat()
            s = (shape.a+shape.b+shape.c)/2
            area = math.sqrt(s*(s-shape.a)*(s-shape.b)*(s-shape.c))
            shapename = "Triangle"
            break
        elif (x=='C'):
            print ("\nPlease input the radius")
            shape.a=CheckForFloat()
            area = math.pi*shape.a**2
            shapename = "Circle"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Area of the %s is: %s\n" %(shapename,area))

def PerimeterMath():
    while True:
        print ("\nPerimeter")
        print ("Enter 'S' for Square, 'R' for Rectangle, 'T' for Triangle,\n'RT' for Right Triangle or 'C' for Circle")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='S'): #for squares a is the side length
            print ("\nPlease input the side length")
            shape.a = CheckForFloat()
            perimeter = shape.a*4
            shapename = "Square"
            break
        elif (x=='R'): #for rectangles a is length b is width
            print ("\nPlease input the length")
            shape.a = CheckForFloat()
            print ("\nPlease input the width")
            shape.b = CheckForFloat()
            perimeter = 2*shape.a + 2*shape.b
            shapename = "Rectangle"
            break
        elif (x=='RT'): #for right triangle a is base and b is height
            print ("\nPlease input the base")
            shape.a = CheckForFloat()
            print ("\nPlease input the height")
            shape.b = CheckForFloat()
            perimeter = shape.a + shape.b + math.sqrt(shape.a**2 + shape.b**2)
            shapename = "Right Triangle"
            break
        elif (x=='T'):
            print ("\nPlease input side A length")
            shape.a=CheckForFloat()
            print ("\nPlease input side B length")
            shape.b=CheckForFloat()
            print ("\nPlease input side C length")
            shape.c=CheckForFloat()
            perimeter = shape.a + shape.b + shape.c
            shapename = "Triangle"
            break
        elif (x=='C'):
            print ("\nPlease input the radius")
            shape.a=CheckForFloat()
            perimeter = 2 * math.pi * shape.a
            shapename = "Circle"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Perimeter of the %s is: %s\n" %(shapename,perimeter))

def VolumeMath():
    while True:
        print ("\nVolume")
        print ("Enter 'C' for Cube, 'RRP' for Right Rectangular Prism, 'PR' for Prism , 'CY' for Cylinder,\n'PY' for Pyramid, 'CO' for Cone or 'S' for Sphere")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='C'): #for squares a is the side length
            print ("\nPlease input the side length")
            shape.a = CheckForFloat()
            volume = shape.a**3
            shapename = "Cube"
            break
        elif (x=='RRP'): #for rectangles a is length b is width
            print ("\nPlease input the length")
            shape.a = CheckForFloat()
            print ("\nPlease input the width")
            shape.b = CheckForFloat()
            print ("\nPlease input the height")
            volume = shape.a*shape.b*shape.c
            shapename = "Rectangle"
            break
        elif (x=='PR') or (x=='CY'): #for right triangle a is base and b is height
            print ("\nPlease input the area of the base")
            shape.a = CheckForFloat()
            print ("\nPlease input the height")
            shape.b = CheckForFloat()
            volume = shape.a*shape.b
            if (x=='PR'): shapename = "Prism"
            else: shapename = "Cylinder"
            break
        elif (x=='PY') or (x=='CO'):
            print ("\nPlease input the area of the base")
            shape.a = CheckForFloat()
            print ("\nPlease input the height")
            shape.b = CheckForFloat()
            volume = (1/3) * shape.a * shape.b
            if (x=='PY'): shapename = "Pyramid"
            else: shapename = "Cone"
            break
        elif (x=='S'):
            print ("\nPlease input the radius")
            shape.a=CheckForFloat()
            volume = (4/3) * math.pi * (shape.a**3)
            shapename = "Sphere"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Area of the %s is: %s\n" %(shapename,volume))

def ResetShape():
    shape.a=0
    shape.b=0
    shape.c=0


global shape
shape = Shape(0,0,0)
while True:
    print ("Main Menu")
    print ("Enter 'A' for Area, 'P' for Perimeter or 'V' for volume.")
    print ("Enter 'Q' to quit")
    x = input("User=> ").upper()

    if (x=='A'):
        ResetShape()
        AreaMath()
    elif (x=='P'):
        ResetShape()
        PerimeterMath()
    elif (x=='V'):
        ResetShape()
        VolumeMath()
    elif (x=='Q'):
        break
    else:
        print ("Error: Not a Valid Command")
