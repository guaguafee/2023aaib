# SOIT107_BASE_017剩餘啤酒有幾手又幾瓶
a = int(input())
b = int(input())

ans = a - b*6
print( ans//6, ans%6, end='')