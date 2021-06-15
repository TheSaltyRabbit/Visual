#Created by Christian Mascunana 06/14/2021
import math

class Shape:
    def __init__(self, sides):
        self.sides = sides

def CheckForFloat():
    while True:
        try:
            x = float(input("User=> "))
            break
        except ValueError:
            print ("Error: Entry was not a number")
    return x

def GetSides(x,name1, name2, name3):
    name = [name1,name2,name3]
    for i in range (0,x):
        print ("\nPlease input %s"%(name[i]))
        shape.sides[i]=CheckForFloat()

def AreaMath():
    while True:
        print ("\nArea")
        print ("Enter 'S' for Square, 'R' for Rectangle, 'T' for Triangle,\n'RT' for Right Triangle or 'C' for Circle")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='S'):
            GetSides(1,"The Length of the Side","","")
            shape.sides[3] = shape.sides[0]**2
            shapename = "Square"
            break
        elif (x=='R'):
            GetSides(2,"the Length","the Width","")
            shape.sides[3] = shape.sides[0]*shape.sides[1]
            shapename = "Rectangle"
            break
        elif (x=='RT'):
            GetSides(2,"the Base","the Height","")
            shape.sides[3] = 0.5*shape.sides[0]*shape.sides[1]
            shapename = "Right Triangle"
            break
        elif (x=='T'):
            GetSides(3,"Side A","Side B","Side C")
            s = (shape.sides[0]+shape.sides[1]+shape.sides[2])/2
            shape.sides[3] = math.sqrt(s*(s-shape.sides[0])*(s-shape.sides[1])*(s-shape.sides[2]))
            shapename = "Triangle"
            break
        elif (x=='C'):
            GetSides(1,"the Radius","","")
            shape.sides[3] = math.pi*shape.sides[0]**2
            shapename = "Circle"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Area of the %s is: %s\n" %(shapename,shape.sides[3]))  

def PerimeterMath():
    while True:
        print ("\nPerimeter")
        print ("Enter 'S' for Square, 'R' for Rectangle, 'T' for Triangle,\n'RT' for Right Triangle or 'C' for Circle")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='S'):
            GetSides(1,"The Length of the Side","","")
            shape.sides[3] = shape.sides[0]*4
            shapename = "Square"
            break
        elif (x=='R'):
            GetSides(2,"the Length","the Width","")
            shape.sides[3] = 2*shape.sides[0] + 2*shape.sides[1]
            shapename = "Rectangle"
            break
        elif (x=='RT'):
            GetSides(2, "the Base", "the Height","")
            shape.sides[3] = shape.sides[0] + shape.sides[1] + math.sqrt(shape.sides[0]**2 + shape.sides[1]**2)
            shapename = "Right Triangle"
            break
        elif (x=='T'):
            GetSides(3, "Side A", "Side B", "Side C")
            shape.sides[3] = shape.sides[0] + shape.sides[1] + shape.sides[2]
            shapename = "Triangle"
            break
        elif (x=='C'):
            GetSides(1, "the Radius","","")
            shape.sides[3] = 2 * math.pi * shape.sides[0]
            shapename = "Circle"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Perimeter of the %s is: %s\n" %(shapename,shape.sides[3]))  

def VolumeMath():
    while True:
        print ("\nVolume")
        print ("Enter 'C' for Cube, 'RRP' for Right Rectangular Prism, 'PR' for Prism , 'CY' for Cylinder,\n'PY' for Pyramid, 'CO' for Cone or 'S' for Sphere")
        print ("Enter B to return to the Main Menu")
        x = input("User=> ").upper()
        if (x=='C'):
            GetSides(1, "the Length of the Side","","")
            shape.sides[3] = shape.sides[0]**3
            shapename = "Cube"
            break
        elif (x=='RRP'):
            GetSides(3,"the Length","the Width","the Height")
            shape.sides[3] = shape.sides[0]*shape.sides[1]*shape.sides[2]
            shapename = "Rectangle"
            break
        elif (x=='PR') or (x=='CY') or (x=='PY') or (x=='CO'):
            GetSides(2,"the Area of the Base","the Height","")
            if (x=='PR') or (x=='CY'):
                shape.sides[3] = shape.sides[0]*shape.sides[1]
                if (x=='PR'): shapename = "Prism"
                else: shapename = "Cylinder"
            else:
                shape.sides[3] = (1/3) * shape.sides[0] * shape.sides[1]
                if (x=='PY'): shapename = "Pyramid"
                else: shapename = "Cone" 
            break
        elif (x=='S'):
            GetSides(1, "the Radius","","")
            shape.sides[3] = (4/3) * math.pi * (shape.sides[0]**3)
            shapename = "Sphere"
            break
        else:
            print ("Error: Invalid Entry")

    print ("The Volume of the %s is: %s\n" %(shapename,shape.sides[3]))

def ResetShape():
    shape.sides = [0,0,0,0]

global shape
shape = Shape([0,0,0,0])
while True:
    ResetShape()
    print ("Main Menu")
    print ("Enter 'A' for Area, 'P' for Perimeter or 'V' for Volume.")
    print ("Enter 'Q' to quit")
    x = input("User=> ").upper()

    if (x=='A'):
        AreaMath()
    elif (x=='P'):
        PerimeterMath()
    elif (x=='V'):
        VolumeMath()
    elif (x=='Q'):
        break
    else:
        print ("Error: Not a Valid Command")