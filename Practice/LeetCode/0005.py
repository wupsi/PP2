class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if j != 0:
                    if s[i:-j] == s[i:-j][::-1]:
                        if len(ans) < len(s[i:-j]):
                            ans = s[i:-j]
                else:
                    if s[i:] == s[i:][::-1]:
                        if len(ans) < len(s[i:]):
                            ans = s[i:]
        return ans
