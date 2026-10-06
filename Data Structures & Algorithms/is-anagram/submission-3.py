class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            count_s[s[i]] = count_s.get(s[i],0) + 1
            count_s[t[i]] = count_s.get(t[i],0) - 1
        return all(v == 0 for v in count_s.values())

