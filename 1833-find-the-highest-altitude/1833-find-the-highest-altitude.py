class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        alt = 0
        for g in gain:
            nextalt = g+alt
            highest = max(nextalt, highest)
            alt = nextalt
        return highest
