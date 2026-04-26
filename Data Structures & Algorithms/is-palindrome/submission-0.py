class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[^a-zA-Z0-9]" 
        result = re.sub(regex, "", s).lower()
        for i in range(len(result)//2):
            if result[i] != result[len(result)-1-i]: return False
        return True