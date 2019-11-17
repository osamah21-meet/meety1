import math
x=input()
y=input()

z=math.pow(int(x),int(y))
d=math.sqrt(z)
print (z)
print (d)

while d < 100000:

	d = d + 1
	print(d)
if d>10:
	d=d*10
