#SOIT107_ADVANCE_014奇數之和
a = int(input())
ans = 0

for i in range(1, a+1, 2):
	ans += i
	
print(ans, end='')