class Solution:
    def findAnagrams(self, s, p):
        result = []
        len1 = len(p)
        len2 = len(s)
        if len1 > len2:
            return result
        
        freq = defaultdict(int)
        for i in p:
            freq[i] += 1

        for i in range(len1):
            if s[i] in p:
                freq[s[i]] -= 1
            
        for i in range(-1, len2 - len1):
            if i > -1:
                if s[i] in p:
                    freq[s[i]] += 1
                if s[i + len1] in p:
                    freq[s[i + len1]] -= 1
                    
            if all(v == 0 for v in freq.values()):
                result.append(i + 1)
                
                
        return result
