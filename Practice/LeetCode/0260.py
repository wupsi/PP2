class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        ans = []
        for key, value in d.items():
            if value == 1:
                ans.append(key)
        return ans