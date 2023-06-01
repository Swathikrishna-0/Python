# Given coffcients a,b, and c of quadratic equation ax^2+bx^+c=0. FInd the roots r1,r2 of the equation.

# input 
# a=1 b=-5 c=6
# output 
# r1 = (5-(25-24))/2
# r1 = 3 
# r2 = (5-(25-24))/2 
# r2 = 2

a = int(input())
b = int(input())
c = int(input())
r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a) 
print(r1)
print(r2)