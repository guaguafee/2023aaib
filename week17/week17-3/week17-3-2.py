# 瘋狂程設-----SOIT108_ADVANCE_014計算級數的值
n = int(input())
total = 0
for i in range(n+1):
	total += 2*i + 1
print( f'f({n})={total}', end='')
# print(total, end='')