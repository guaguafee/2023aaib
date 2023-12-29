# SOIT108_BASE_004判斷座標的象限
x,y = list(map(int, input().split()))
if x>0 and y>0: print(1)
if x>0 and y<0: print(4)
if x<0 and y<0: print(3)
if x<0 and y>0: print(2)