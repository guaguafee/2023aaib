# SOIT108_ADVANCE_001判斷平方數
a = int(input())
ans = 0
for i in range(1,1001):
	if i*i == a:
		ans = i
print(ans, end='')