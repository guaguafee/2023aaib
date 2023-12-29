# SOIT107_ADVANCE_012星星等腰三角
a = int(input())

for i in range(a):
	space = a - 1 - i
	for k in range(space):
		print(' ', end='')
		
	star = 2 * i + 1
	for k in range (star):
		print('*', end='')
	
	print() #print(i)