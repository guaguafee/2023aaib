# 瘋狂程設-----SOIT108_ADVANCE_014B拆解輸入的正整數
a = int(input())

ten = 1
while a>0:
	print(a%10*ten, end=' ')
	ten = ten * 10
	a = a//10