class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 還沒寫完，不要送出
        if n <= 0: return False # 現在成功了
        while n > 1: # 因為1是2的0次方不用再除了
            if n%2 != 0: #竟然餘數不是0
                return False # 失敗
            n = n // 2
        # 經過樓上檢查，如沒錯
        return True # 成功