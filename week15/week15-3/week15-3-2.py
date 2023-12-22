#SOIT107_ADVANCE_003計算一列整數的總和
ans = 0
while True:
	print('Enter an integer ( 999 to end ): ')
	a = int(input())
	if a==999: break
	ans += a
	
print('The total is:', ans, end='')