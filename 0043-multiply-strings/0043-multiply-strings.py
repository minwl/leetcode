class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.convert(num1)
        num2 = self.convert(num2)
        mul = num1*num2
        ans = ""
        if mul == 0 :
            return "0"
        while mul != 0:
            digit = mul%10
            mul = mul//10
            ans += chr(digit+48)
        return ans[::-1]
    
    
    def convert(self, num):
        ten = 1
        i = len(num)-1
        ans = 0
        while i >= 0:
            ans += (ord(num[i])-48)*ten
            ten *= 10
            i -= 1
        return ans