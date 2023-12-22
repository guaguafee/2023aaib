#SOIT107_ADVANCE_011字串中的數字個數
a = input()
ans = 0
for c in a:
		#if c.isdigit()
		if c>='0' and c<='9': ans+=1
print(ans)