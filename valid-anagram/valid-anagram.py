class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        for strs in s:
            count=count_s.get(strs)
            if count is None:
                count_s[strs] = 1
                continue
            count_s[strs]+=1
        count_t={}
        for strs in t:
            count=count_t.get(strs)
            if count is None:
                count_t[strs] = 1
                continue
            count_t[strs]+=1
        if len(count_s) ==len(count_t):
            for i in count_s:
                if i not in count_t:
                    return False
                if count_s[i] != count_t[i]:
                    return False
            return True
        else:
            return False