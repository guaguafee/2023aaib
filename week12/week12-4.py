class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0 # 迴圈前面ans=0
        while n>0: # 剝皮法,一次剝一層(第87週)
            ans += n%2 # 剝下來的屑屑,收起起來
            n = n//2 # 洋蔥剝皮後,變小了
        return ans # 迴圈後面ans拿來用