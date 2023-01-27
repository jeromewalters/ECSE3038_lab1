import math
#finding area of a cirlce
def area_of_circle(r):
    a = math.pi * r**2
    return a
print (area_of_circle(5))

#finiding the volume of a shere
def volume_of_sphere(r):
    v = (4*(math.pi * r**3))/3
    return v
print (volume_of_sphere(56))

#finding sides of a rigt angle triangle
def pythag(a,b):
    c = math.sqrt(a**2 + b**2)
    return c
print(pythag(2,3))

def summation():
    result = 0
    
    for n in range(1,21):
       result += math.sqrt(((n + 5)**5) / 2) #or result = math.sqrt(((n + 5)**5) / 2) + result

    return result
print(summation())

