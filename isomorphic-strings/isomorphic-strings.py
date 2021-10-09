class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        d1=dict()
        d2=dict()
        for i in range(n):
            key,val=s[i],t[i]
            if key in d1:
                if d1[key] != val:
                    return False
            else:
                if val in d2:
                    return False
                d1[key],d2[val]=val,key
        return True
                