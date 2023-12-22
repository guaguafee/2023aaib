#SOIT107_ADVANCE_015兩數間可被7整除的數
a, b = list(map(int, input().split()))

for i in range(a, b+1):
	if i%7==0:
		print(i, end=' ')