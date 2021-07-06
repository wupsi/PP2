class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        if not s:
            return 0
        else:
            for j in range(len(s)):
                sub = ''
                for i in s[j:]:
                    if i not in sub:
                        sub += i
                    else:
                        break
                if len(sub) > len(ans):
                    ans = sub
        
        return len(ans)