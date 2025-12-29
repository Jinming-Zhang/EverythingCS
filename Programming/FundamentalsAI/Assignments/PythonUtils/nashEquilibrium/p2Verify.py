x = 1
y = 2
z = 3

r1 = 1.5/6
p1 = 2.5/6
s1 = 2.0/6

r2 = 3.0/6
p2 = 2.0/6
s2 = 1.0/6

payOffRose = x*p1*r2-z*p1*s2-x*r1*p2+y*r1*s2+z*s1*p2-y*s1*r2
print(payOffRose)
