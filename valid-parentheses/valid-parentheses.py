class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(',
           ']':'[',
           '}':'{'
        }
        for i in s:                
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if stack:
                    if stack[-1] != d[i]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return len(stack) == 0