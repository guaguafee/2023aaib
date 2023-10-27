class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #長度不一樣，當然失敗
        d = {}
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1

        for c in t:
            if c not in d: # 右邊有字母，不再字典裡
                return False # 失敗
            if d[c] == 0: # 字母已用完
                return False # 失敗
            else:
                d[c] = d[c] - 1

        return True