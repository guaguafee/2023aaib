s = {1,2,3,4} # 第1種用大括號
print(s)
s = set( (1,3,5,7) ) # 第2種用set()裡放一開始要加入的東西，可用圓括號
print(s)
s = set( [1,2,4,3] ) # 第2種的set()裡也可以放[方括號]list的陣列的東西
print(s)
s = set( 'hello' ) # 第2種的set()裡也可以放[字串]會把他一個一個拆開來
print(s)

# 下面試試 .add() 和 remove
s.add(100)
print(s)
s.remove('h')
print(s)