class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            c=count.get(i)
            if c is None:
                count[i]=1
                continue
            count[i]+=1
        lst=[]
        for idx, n in enumerate(s):
            if count[n]==1:
                lst.append(idx)
        if lst:
            return lst[0]
        else:
            return -1