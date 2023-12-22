# leetcode-----1422.Maximum score after splitting
class Solution:
    def maxScore(self, s: str) -> int:
# 現在要試著模擬看看方法
        N = len(s)
        zero = 0
        one = 0
        for i in range(N):
            if s[i]=='1': one += 1

        #print('一開始時，都在右邊，統計結果','zero', zero, 'one', one)
        ans = 0
        for i in range(N-1):
            if s[i]=='0':
                zero += 1
            if s[i]=='1':
                one -= 1
            #print('中間過程中，','zero', zero, 'one', one)
            ans = max( ans, zero+one)
        return ans