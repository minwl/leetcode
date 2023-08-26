class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i, j = 0, 0
        length = len(chars)
        while i < length:
            count = 0
            
            while j < length and chars[i] == chars[j]:
                if chars[i] == chars[j]:
                    count += 1
                j += 1
            
            digit = list(str(count))
            if count > 1:
                for k in range(i+1, j):
                    chars.pop(i+1)
                    length -= 1
                for k in range(len(digit)):
                    i += 1
                    chars.insert(i, digit[k])
                    length += 1
            i += 1
            j = i
        
        return len(chars)



