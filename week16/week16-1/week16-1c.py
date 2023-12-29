word = 'cat'
wordH = {}
for c in word:
  if c in wordH:
    wordH[c] += 1
  else:
    wordH[c] = 1
  print(c, wordH)