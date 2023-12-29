# SOIT108_ADVANCE_002B三數組合
a = list(map(int, input().split()))
a.sort()
ans = a[2]*100 + a[1]*10 + a[0] + 1
print(ans , end='')