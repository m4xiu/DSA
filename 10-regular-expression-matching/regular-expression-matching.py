class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import cache
        s_length = len(s)
        p_length = len(p)
      
        @cache
        def match_helper(s_index: int, p_index: int) -> bool:
            if p_index >= p_length:
                return s_index == s_length
            if p_index + 1 < p_length and p[p_index + 1] == '*':
                skip_pattern = match_helper(s_index, p_index + 2)
                match_current = (s_index < s_length and 
                                (s[s_index] == p[p_index] or p[p_index] == '.') and 
                                match_helper(s_index + 1, p_index))
              
                return skip_pattern or match_current
            return (s_index < s_length and 
                   (s[s_index] == p[p_index] or p[p_index] == '.') and 
                   match_helper(s_index + 1, p_index + 1))
        return match_helper(0, 0)
