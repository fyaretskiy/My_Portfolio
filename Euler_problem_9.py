
#make lists first for all that satisfy a**2 + b**2 = C**2
#where a < b < c
#no the first thing to check is all numbers less than 10000
#that are sq numbers
global a, b, c
a = 1
b = 2
c = 3

# for i in a:
# 	for i in b:
# 		if a < b:
# 			for i in c:
# 				if b < c and a + b + c == 1000:
# 					print a, b, c

while a < 500:
	while b < 500:
		while c < 500:
			c = c + 1
			if a < b < c and a**2 + b**2 == c**2 and a + b + c == 1000:
				print a, b, c, a * b * c
		b = b + 1
		c = 1
	a = a + 1
	b = 1
	