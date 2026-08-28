class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        f = [0] * 26
        for c in s: f[ord(c) - ord('a')] += 1

        oddc = ''
        for i, freq in enumerate(f):
            if freq % 2 == 1:
                if oddc == '': oddc = chr(i + ord('a'))
                else: return ''
            f[i] //= 2
        
        p = []
        for i in range(n // 2):
            valid = False
            for ci in range(26):
                c = chr(ci + ord('a'))
                if not f[ci] or c < target[i]: continue
            
                if c > target[i]:
                    f[ci] -= 1
                    p.append(c)
                    for cci in range(26):
                        if not f[cci]: continue
                        p.append(f[cci] * chr(cci + ord('a')))
                    return "".join(p + [oddc] + p[::-1])
                
                f[ci] -= 1
                p.append(c)
                copy = p[::]
                for cci in range(25, -1, -1):
                    if not f[cci]: continue
                    copy.append(f[cci] * chr(cci + ord('a')))
                if "".join(copy + [oddc] + copy[::-1]) > target:
                    valid = True
                    break
                f[ci] += 1
                p.pop()
            
            if not valid: return ""
        
        out = "".join(p + [oddc] + p[::-1])
        return out if out > target else ''


            
    

            
            




































                


            
    

            
            




































                