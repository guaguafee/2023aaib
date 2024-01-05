# 瘋狂程設-----SOIT108_BASE_007把數字倒著印出來
a = list(map(int, input().split()))
for i in range(10-1,-1,-1):
	print(a[i], end=' ')