word = 'cat'
chars = 'atach'
H = {}
for c in chars:
  if c in H:
    H[c] += 1 # 多1字母
  else: # 未出現過
    H[c] = 1 #第1個
  print(c, H)