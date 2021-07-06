class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = nums1 + nums2
        all_nums.sort()
        
        if len(all_nums) % 2 == 0:
            return(((all_nums[(len(all_nums)//2)-1]) + (all_nums[(len(all_nums)//2)])) / 2)
        
        elif len(all_nums) == 1:
            return(float(all_nums[0]))
        
        else:
            return(float(*all_nums[(len(all_nums)-1)//2:-((len(all_nums)-1)//2)]))