# SOIT108_ADVANCE_007區間測速-超速之王
a = list(map(int, input().split()))
fast = min(a)
for i in range(10):
	if a[i] == fast:
		ans = i
		print(ans+1, int(1.2*60*60/fast))