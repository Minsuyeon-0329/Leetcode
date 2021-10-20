class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx=0
        sm=0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                sm-=1
            else:
                sm+=1
            if sm in d:
                mx=max(mx,i-d[sm])
            else:
                d[sm]=i
        return mx