class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        res = list(set(nums))
        res.sort()
        k = len(res)
        for i in range(k):
            if nums[i] != res[i]:
                nums[i] = res[i]
        
        return k