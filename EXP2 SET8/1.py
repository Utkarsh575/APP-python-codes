from math import sqrt
def hypotaneous (  s1 , s2):
    return sqrt(a**2 + b**2)
    
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = hypotaneous(a,b)
print("The length of the hypotenuse is:", c )
