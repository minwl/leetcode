class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1 and n not in check:
            check.add(n)
            n = self.digit(n)
        if n == 1 : return True
        else : return False
        
        
    def digit(self, n):
        digit = []
        while n > 0:
            r = n%10
            digit.append(r)
            n = n//10
            
        sum = 0
        for x in digit:
            sum += x * x
        return sum