class Solution:
    def isPalindrome(self, x: int) -> bool:
        return bool(str(x) == str(x)[::-1])