# a = [1, 1, 2, 3, 5, 8, 13, 21]
a = [1, 1]
for i in range(2, 100): # 課本CH3 list
  a.append( a[i-1] + a[i-2] ) # 利用 .append() 在後面加1項
  # a[i] = a[i+1] + a[i-2]

print(a)