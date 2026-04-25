class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_groups = {}
        for word in strs:
            lex_tuple=[0 for _ in range(26)]
            for letter in word:
                lex_tuple[ord(letter)-97] +=1
            lex_tuple = tuple(lex_tuple)
            if lex_tuple not in word_groups:
                word_groups[lex_tuple] = [word]
            else: word_groups[lex_tuple].append(word)
        return [word_group for word_group in word_groups.values()]
