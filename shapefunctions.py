import math
# area of a circle
def getAreaOfCircle(radius):
    return math.pi * (radius**2)
def getCircumferenceOfCircle(radius):
    return 2 * math.pi * radius
def getAreaOfSquare(side):
    return side**2
def getAreaOfTriangle(base, height):
    return ((base*height)/2)


# print statements below
print(getAreaOfCircle(2))  # 12.566370614359172
print(getCircumferenceOfCircle(4))  # 25.132741228718345
print(getAreaOfSquare(4))  # 16
print(getAreaOfTriangle(4, 2))  # 4.0