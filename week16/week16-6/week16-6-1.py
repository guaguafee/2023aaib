# SOIT108_ADVANCE_004求11 +22+33+…+nn。
a = int(input())
ans = 0
for i in range(1,a+1):
	ans += 11*i
print(ans, end='')