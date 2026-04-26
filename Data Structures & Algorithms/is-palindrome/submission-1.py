class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[^a-zA-Z0-9]" 
        result = re.sub(regex, "", s).lower()
        return result == result[::-1]