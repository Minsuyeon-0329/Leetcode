class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() 
        if len(pattern) != len(words): 
            return False
        bijection = {} 
        for j,char in enumerate(pattern): 
            if not (char in bijection):  
                if words[j] in bijection.values(): 
                    return False
                bijection[char] = words[j]
            else: 
                if bijection[char] != words[j] : 
                    return False
                
        return True