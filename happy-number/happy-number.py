class Solution:
    def isHappy(self, n: int) -> bool:
        h=0
        a=[]
        while True:
            for i in str(n):
                h+=int(i)**2
            if h==1:
                return True
                break
            else:
                if h in a:
                    return False
                    break
                else:
                    a.append(h)
                    n,h=h,0
            