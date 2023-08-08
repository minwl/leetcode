class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = dict()
        i = 0
        ans = []
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                
        ans= sorted(freq.keys(), key = lambda x : (-freq[x], x))
        return ans[:k]