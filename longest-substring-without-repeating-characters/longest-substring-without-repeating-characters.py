class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        b=1
        c=0
        for i in range(len(s)):
            a.append(s[i])
    
            for j in range(i+1,len(s)):
                if s[j] not in a:
                    b+=1
                    a.append(s[j])
                else:
                    a=[]
                    break

            c=max(c,b)
            b=1
        return c                    