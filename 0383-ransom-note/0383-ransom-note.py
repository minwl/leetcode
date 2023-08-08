class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        magcount = {}
        for char in magazine:
            magcount[char] = magcount.get(char, 0) + 1
        
        for note in ransomNote:
            if note not in magcount or magcount[note] <= 0 :
                return False
            else:
                magcount[note] -= 1
        return True