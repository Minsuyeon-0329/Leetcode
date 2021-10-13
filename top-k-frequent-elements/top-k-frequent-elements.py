class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            c=count.get(n)
            if c is None:
                count[n]=1
            count[n]+=1
        count=sorted(count.items(),key=lambda x : x[1], reverse = True)
        lst=[]
        for i in range(k):
            lst.append(list(count)[i][0])
        return lst