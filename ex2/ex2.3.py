from math import pi,tan,cos

y0 = 1
x = 0.5
theta = 80 * pi/180
g = 9.81
v0 = 44
y = y0 + x * tan(theta) - (g*x**2)/(2*(v0*cos(theta))**2)
print(y)