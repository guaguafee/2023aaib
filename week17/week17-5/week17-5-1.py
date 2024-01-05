# 瘋狂程設-----SOIT108_BASE_010水杯接水
a, b = list(map(int, input().split()))

# print(a/b)
ans = a//b
if a%b>0: ans += 1
print( ans, end='' )