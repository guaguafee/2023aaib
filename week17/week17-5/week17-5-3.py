# SOIT108_BASE_013計算一組任意數目的整數的總和
a = list(map(int, input().split()))
ans = 0
for b in a:
	if b>0: ans += b
print(ans, end='')