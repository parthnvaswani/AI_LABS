# 1. Write a Python program to convert degree to radian. 
# Note : The radian is the standard unit of angular measure, used in many areas of mathematics. An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle one radian is just under 57.3 degrees (when the arc length is equal to the radius).
# Test Data:
# Degree : 15
# Expected Result in radians: 0.2619047619047619
import math
degree = float(input("Input degrees: "))
print(math.radians(degree))

# 2. Write a Python program to convert radian to degree. 
# Test Data:
# Radian : .52
# Expected Result : 29.781818181818185

radian = float(input("Input radians: "))
print(math.degrees(radian))

# 3. Write a Python program to calculate the area of a trapezoid. 
# Note : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so.
# Test Data:
# Height : 5
# Base, first value : 5
# Base, second value : 6
# Expected Output: Area is : 27.5

height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)

# 4. Write a Python program to calculate the area of a parallelogram. 
# Note : A parallelogram is a quadrilateral with opposite sides parallel (and therefore opposite angles equal). A quadrilateral with equal sides is called a rhombus, and a parallelogram whose angles are all right angles is called a rectangle.
# Test Data:
# Length of base : 5
# Height of parallelogram : 6
# Expected Output: Area is : 30.0

base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)

# 5. Write a Python program to calculate surface volume and area of a cylinder. 
# Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.
# Test Data:
# volume : Height (4), Radius(6)
# Expected Output:
# Volume is : 452.57142857142856
# Surface Area is : 377.1428571428571

height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = math.pi * radian * radian * height
sur_area = ((2*math.pi*radian) * height) + ((math.pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)

# 6. Write a Python program to calculate surface volume and area of a sphere. 
# Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball.
# Test Data:
# Radius of sphere : .75
# Expected Output :
# Surface Area is : 7.071428571428571
# Volume is : 1.7678571428571428

radian = float(input('Radius of sphere: '))
sur_area = 4 * math.pi * radian **2
volume = (4/3) * (math.pi * radian ** 3)
print("Surface Area is: ", sur_area)
print("Volume is: ", volume)

# 7. Write a Python program to calculate arc length of an angle. 
# Note: In a planar geometry, an angle is the figure formed by two rays, called the sides of the angle, sharing a common endpoint, called the vertex of the angle. Angles formed by two rays lie in a plane, but this plane does not have to be a Euclidean plane.
# Test Data:
# Diameter of a circle : 8
# Angle measure : 45
# Expected Output :
# Arc Length is : 3.142857142857143

def arclength():
    diameter = float(input('Diameter of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    arc_length = (math.pi*diameter) * (angle/360)
    print("Arc Length is: ", arc_length)

arclength()

# 8. Write a Python program to calculate the area of the sector. 
# Note: A circular sector or circle sector, is the portion of a disk enclosed by two radii and an arc, where the smaller area is known as the minor sector and the larger being the major sector.
# Test Data:
# Radius of a circle : 4
# Angle measure : 45
# Expected Output:
# Sector Area: 6.285714285714286

def sectorarea():
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (math.pi*radius**2) * (angle/360)
    print("Sector Area: ", sur_area)

sectorarea()

# 9. Write a Python program to calculate the discriminant value. 
# Note: The discriminant is the name given to the expression that appears under the square root (radical) sign in the quadratic formula.
# Test Data:
# The x value : 4
# The y value : 0
# The z value : -4
# Expected Output:
# Two Solutions. Discriminant value is : 64.0

def discriminant():
    x_value = float(input('The x value: '))
    y_value = float(input('The y value: '))
    z_value = float(input('The z value: '))
    discriminant = (y_value**2) - (4*x_value*z_value)
    if discriminant > 0:
        print('Two Solutions. Discriminant value is:', discriminant)
    elif discriminant == 0:
        print('One Solution. Discriminant value is:', discriminant)
    elif discriminant < 0:
        print('No Real Solutions. Discriminant value is:', discriminant)

discriminant()

# 10. Write a Python program to find the smallest multiple of the first n numbers. Also, display the factors. 
# Test Data:
# If n = (13)
# Expected Output :
# [13, 12, 11, 10, 9, 8, 7]
# 360360

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
                
print(smallest_multiple(13))

# 11. Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.(default value of number=2). 
# Test Data:
# If sum_difference(12)
# Expected Output :
# 5434

def sum_difference(n=2):
    sum_of_squares = 0
    square_of_sum = 0
    for num in range(1, n+1):
        sum_of_squares += num * num
        square_of_sum += num

    square_of_sum = square_of_sum ** 2

    return square_of_sum - sum_of_squares

print(sum_difference(12))

# 12. Write a Python program to calculate the sum of all digits of the base to the specified power. 
# Test Data:
# If power_base_sum(2, 100)
# Expected Output :
# 115

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])

print(power_base_sum(2, 100))

# 13. Write a Python program to find out, if the given number is abundant. 
# Note: In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.
# Test Data:
# If is_abundant(12)
# If is_abundant(13)
# Expected Output:
# True
# False

def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n
print(is_abundant(12))
print(is_abundant(13))

# 14. Write a Python program to sum all amicable numbers from 1 to specified numbers. 
# Note: Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself. For example, the proper divisors of 6 are 1, 2, and 3.)
# Test Data:
# If amicable_numbers_sum(9999)
# If amicable_numbers_sum(999)
# If amicable_numbers_sum(99)
# Expected Output:
# 31626
# 504
# 0

def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"

    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit+1):
        if num in amicables:
            continue

        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return sum(amicables)

print(amicable_numbers_sum(9999))
print(amicable_numbers_sum(999))
print(amicable_numbers_sum(99))

# 15. Write a Python program to returns sum of all divisors of a number. 
# Test Data:
# If number = 8
# If number = 12
# Expected Output:
# 7
# 16

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))

# 16. Write a Python program to print all permutations of a given string (including duplicates). 

from itertools import permutations
inp=input("Enter a string to get permutations of it.")
print(list(permutations(inp)))

# 17. Write a Python program to print the first n Lucky Numbers. 
# Lucky numbers are defined via a sieve as follows.
# Begin with a list of integers starting with 1 :
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, . . . .
# Now eliminate every second number :
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, ...
# The second remaining number is 3, so remove every 3rd number:
# 1, 3, 7, 9, 13, 15, 19, 21, 25, ...
# The next remaining number is 7, so remove every 7th number:
# 1, 3, 7, 9, 13, 15, 21, 25, ...
# Next, remove every 9th number and so on.
# Finally, the resulting sequence is the lucky numbers.

n=int(input("Input a Number: "))
List=range(-1,n*n+9,2)
i=2
while List[i:]:
    List=sorted(set(List)-set(List[List[i]::List[i]]))
    i+=1
print(List[1:n+1])

# 18. Write a Python program to computing square roots using the Babylonian method. 
# Perhaps the first algorithm used for approximating √S is known as the Babylonian method, named after the Babylonians, or "Hero's method", named after the first-century Greek mathematician Hero of Alexandria who gave the first explicit description of the method. It can be derived from (but predates by 16 centuries) Newton's method. The basic idea is that if x is an overestimate to the square root of a non-negative real number S then S / x will be an underestimate and so the average of these two numbers may reasonably be expected to provide a better approximation.

def BabylonianAlgorithm(number):
    if(number == 0):
        return 0

    g = number/2.0
    g2 = g + 1
    while(g != g2):
        n = number/ g
        g2 = g
        g = (g + n)/2

    return g
print('The Square root of 0.3 =', BabylonianAlgorithm(0.3))

# 19. Write a Python program to multiply two integers without using the * operator in python. 

def multiply(x, y):
    result=0
    for i in range(0,x):
        result+=y
    return result

print(multiply(3, 5))

# 20. Write a Python program to calculate magic square. 
# A magic square is an arrangement of distinct numbers (i.e., each number is used once), usually integers, in a square grid, where the numbers in each row, and in each column, and the numbers in the main and secondary diagonals, all add up to the same number, called the "magic constant." A magic square has the same number of rows as it has columns, and in conventional math notation, "n" stands for the number of rows (and columns) it has. Thus, a magic square always contains n2 numbers, and its size (the number of rows [and columns] it has) is described as being "of order n".
 
def magic_square_test(my_matrix):
    iSize = len(my_matrix[0])
    sum_list = []
    
    sum_list.extend([sum (lines) for lines in my_matrix])   

    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)  
    
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)

    if len(set(sum_list))>1:
        return False
    return True

m=[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]] 
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(magic_square_test(m))

m=[[2, 7, 6], [9, 5, 1], [4, 3, 7]]
print(magic_square_test(m))

# 21. Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number. 
# In mathematics, the sieve of Eratosthenes, one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.

def sieve_of_Eratosthenes(num):
    limitn = num+1
    not_prime_num = set()
    prime_nums = []

    for i in range(2, limitn):
        if i in not_prime_num:
            continue

        for f in range(i*2, limitn, i):
            not_prime_num.add(f)

        prime_nums.append(i)

    return prime_nums

print(sieve_of_Eratosthenes(100))

# 22. Write a python program to find the next smallest palindrome of a specified number. 

import sys
def Next_smallest_Palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i

print(Next_smallest_Palindrome(99))
print(Next_smallest_Palindrome(1221))

# 23. Write a python program to find the next previous palindrome of a specified number. 

def Previous_Palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
print(Previous_Palindrome(99))
print(Previous_Palindrome(1221))

# 24. Write a Python program to convert a float to ratio. 
# Expected Output :
# 21/5 

from fractions import Fraction
value = 4.2
print(Fraction(value).limit_denominator())

# 25. Write a Python program for nth Catalan Number. 
# In combinatorial mathematics, the Catalan numbers form a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. They are named after the Belgian mathematician Eugène Charles Catalan (1814 –1894).

def catalan_number(num):
    if num <=1:
         return 1
   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
 
for n in range(10):
    print(catalan_number(n))
	
# 26. Write a Python program to print number with commas as thousands separators. 

print("{:,}".format(1000000))
print("{:,}".format(10000))

# 27. Write a Python program to calculate the distance between two points using latitude and longitude. 
# Expected Output :
# Input coordinates of two points:                                        
# Starting latitude: 23.5                                                 
# Ending longitude: 67.5                                                  
# Starting latitude: 25.3                                                 
# Ending longitude: 69.5                                                  
# The distance is 284.73km.

from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)

# 28. Write a Python program to calculate the area of regular polygon. 
# Expected Output :
# Input number of sides: 4                                                
# Input the length of a side: 25                                          
# The area of the polygon is:  625.0000000000001

from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

# 29. Write a Python program to calculate wind chill index. 
# Expected Output :
# Input wind speed in kilometers/hour: 150                                
# Input air temperature in degrees Celsius: 29                            
# The wind chill index is 31 

import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))

# 30. Write a Python program to find the roots of a quadratic function. 
# Expected Output :
# Quadratic function : (a * x^2) + b*x + c                                
# a: 25                                                                   
# b: 64                                                                   
# c: 36                                                                   
# There are 2 roots: -0.834579 and -1.725421

from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")

# 31. Write a Python program to convert a binary number to decimal number. 
# Expected Output :
# Input a binary number: 101011                                           
# The decimal value of the number is 43

b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)

# 32. Write a Python program to print a complex number and its real and imaginary parts. 
# Expected Output :
# Complex Number:  (2+3j)                                                          
# Complex Number - Real part:  2.0                                                 
# Complex Number - Imaginary part:  3.0

cn = complex(2,3)
print("Complex Number: ",cn)
print("Complex Number - Real part: ",cn.real)
print("Complex Number - Imaginary part: ",cn.imag)

# 33. Write a Python program to add, subtract, multiply and division of two complex numbers. 
# Expected Output :
# Addition of two complex numbers :  (7-4j)                                        
# Subtraction of two complex numbers :  (1+10j)                                    
# Multiplication of two complex numbers :  (33-19j)                                
# Division of two complex numbers :  (-0.15517241379310348+0.6379310344827587j)

print("Addition of two complex numbers : ",(4+3j)+(3-7j))
print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
print("Division of two complex numbers : ",(4+3j)/(3-7j))

# 34. Write a Python program to get the length and the angle of a complex number. 
# Expected Output :
# Length of a complex number:  5.0                                                 
# Complex number Angle:  1.5707963267948966

import cmath
cn = complex(3,4)
#length of a complex number. 
print("Length of a complex number: ", abs(cn))
# gets angle. return in radians, between  [-π, π]
print("Complex number Angle: ",cmath.phase(0+1j) )

# 35. Write a Python program to convert to/from rectangular coordinates to Polar coordinates. 
# Expected Output :
# Polar Coordinates:  (5.0, 0.9272952180016122)                                    
# Polar to rectangular:  (-2+2.4492935982947064e-16j)

import cmath
cn = complex(3,4)
print("Polar Coordinates: ",cmath.polar(cn))

cn1 = cmath.rect(2, cmath.pi)
print("Polar to rectangular: ",cn1)

# 36. Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 
# Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25
# Expected Output :
# Maximum:  7.25                                                                  
# Minimum:  0.04

from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))

# 37. Write a Python program to find the sum of the following decimal numbers and display the numbers in sorted order. 
# Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25
# Expected Output :
# Sum:  20.33                                                                  
# Sorted order:  [Decimal('0.04'), Decimal('2.00'), Decimal('2.45'), Decimal('2.45'
# ), Decimal('2.69'), Decimal('3.45'), Decimal('7.25')]

from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Sum: ", sum(data))
print("Sorted order: ", sorted(data))

# 38. Write a Python program to get the square root and exponential of a given decimal number. 
# Decimal number : 1.44
# Expected Output :
# Square root of  1.44  is : 1.2                                                   
# exponential of  1.44  is : 4.220695816996552825673328929

from decimal import *
x = Decimal('1.44')
print("Square root of ",x, " is :", x.sqrt())
print("exponential of ",x, " is :", x.exp())

# 39. Write a Python program to retrieve the current global context (public properties) for all decimal. 
# Expected Output :
# Emax     = 999999                                                                
# Emin     = -999999                                                               
# capitals = 1                                                                  
# prec     = 28                                                                  
# rounding = ROUND_HALF_EVEN                                                       
# flags    = <class 'decimal.InvalidOperation'>: False  
# ........

import decimal
context = decimal.getcontext()
print('Emax     =', context.Emax)
print('Emin     =', context.Emin)
print('capitals =', context.capitals)
print('prec     =', context.prec)
print('rounding =', context.rounding)
print('flags    =')
for x, y in context.flags.items():
    print('  {}: {}'.format(x, y))
print('traps    =')
for x, y in context.traps.items():
    print('  {}: {}'.format(x, y))

# 40. Write a Python program to round a specified decimal by setting precision (between 1 and 4). 
# Sample Number : 0.26598
# Original Number : 0.26598
# Precision- 1 : 0.3
# Precision- 2 : 0.27
# Precision- 3 : 0.266
# Precision- 4 : 0.2660
# Expected Output :
# Original Number :  0.26598                                                       
# Precision- 1 : 0.3                                                               
# Precision- 2 : 0.27                                                              
# Precision- 3 : 0.266                                                             
# Precision- 4 : 0.2660

import decimal

d = decimal.Decimal('00.26598')
print("Original Number : ",d)
for i in range(1, 5):
    decimal.getcontext().prec = i
    print("Precision-",i, ':', d * 1)
