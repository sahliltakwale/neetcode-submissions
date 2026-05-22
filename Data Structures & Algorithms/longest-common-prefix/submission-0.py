class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        for i, char in enumerate(strs[0]):
            for word in strs:
                if i >= len(word) or word[i] != char:
                        return ans
            ans += char
        return ans
