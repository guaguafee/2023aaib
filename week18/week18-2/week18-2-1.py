# SOIT108_BASE_012整數向量相加
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(N):
	print( a[i]+b[i], end=' ' )