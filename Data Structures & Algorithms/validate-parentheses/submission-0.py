class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mapping.values():
                st.append(ch)
            else:
                if not st:
                    return False
                
                top = st.pop()
                if mapping[ch] != top:
                    return False
        return len(st) == 0
        