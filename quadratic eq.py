import cmath
a = int(input())
b = int(input())
c = int(input())
d = (b**2)-(4*c*a)
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print("the roots are {} and {}".format(root1,root2))
