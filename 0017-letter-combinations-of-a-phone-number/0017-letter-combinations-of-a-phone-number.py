class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        if digits == "":
            return []
        if len(digits) == 1:
            return phone[int(digits)]
        

        list1 = phone[int(digits[0])]
        list2 = self.letterCombinations(digits[1:])
        
        ans = []
        for x in list1:
            for y in list2:
                ans.append(x+y)
        return ans
        







