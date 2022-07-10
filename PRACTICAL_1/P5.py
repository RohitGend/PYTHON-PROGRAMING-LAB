# to solve quadratic equation
import math
print("For A quadratic equation Enter the values of a,b,c:")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
D=(math.pow(b,2)-(4*a*c))
if(D<0):
    print("The roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are imaginary",sep="")
    exit()
b*=-1
r1=(b+D)/(2*a)
r2=(b-D)/(2*a)
print("The roots of the quadratic equation",a,"x^2 +",b,"x +",c,"are",r1,"and",r2,sep="")