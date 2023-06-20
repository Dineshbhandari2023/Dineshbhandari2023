import math

name = input("Enter your fullname:")
print(name)


def calculate_circle():
  print("Enter the radius of the circle:")
  radius = float(input())

  print("Press A to calculate diameter")
  print("Press B to calculate perimeter")
  print("Press C to calculate area")
  option = input().upper()

  if option == 'A':
    diameter = 2 * radius
    print("Hello " + name + "Diameter of the circle is:", diameter)
  elif option == 'B':
    perimeter = 2 * math.pi * radius
    print("Hello " + name + " Perimeter of the circle is:", perimeter)
  elif option == 'C':
    area = math.pi * radius**2
    print("Hello " + name + " Area of the circle is:", area)
  else:
    print("Invalid option selected.")


def calculate_square():
  print("Enter the side length of the square:")
  side_length = float(input())

  print("Press A to calculate perimeter")
  print("Press B to calculate area")
  option = input().upper()

  if option == 'A':
    perimeter = 4 * side_length
    print("Hello " + name + " Perimeter of the square is:", perimeter)
  elif option == 'B':
    area = side_length**2
    print("Hello " + name + " Area of the square is:", area)
  else:
    print("Invalid option selected.")


def calculate_rectangle():
  print("Enter the length of the rectangle:")
  length = float(input())
  print("Enter the width of the rectangle:")
  width = float(input())

  print("Press A to calculate perimeter")
  print("Press B to calculate area")
  option = input().upper()

  if option == 'A':
    perimeter = 2 * (length + width)
    print("Hello " + name + " Perimeter of the Rectangle is:", perimeter)
  elif option == 'B':
    area = length * width
    print("Hello " + name + " Area of the Rectangle is:", area)
  else:
    print("Invalid option selected.")


# Main program
print("Welcome to the Calculator for geometry problems!")

while True:
  print("Press 0 to exit.")
  print("Press 1 to calculate the properties of a circle.")
  print("Press 2 to calculate the properties of a square.")
  print("Press 3 to calculate the properties of a rectangle.")

  option = int(input())

  if option == 0:
    break
  elif option == 1:
    calculate_circle()
  elif option == 2:
    calculate_square()
  elif option == 3:
    calculate_rectangle()
  else:
    print("Invalid option selected.")
