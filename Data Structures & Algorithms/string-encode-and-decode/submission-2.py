class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return chr(257)
        encoded_str = []
        for sstr in strs:
            encoded_str.append("".join([chr((ord(letter)+1)%256) for letter in sstr]))
        return chr(258).join(encoded_str)

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        encoded_str = s.split(chr(258))
        decoded_str = []
        for sstr in encoded_str:
            decoded_str.append("".join([chr((ord(letter)-1)%256) for letter in sstr]))
        return decoded_str