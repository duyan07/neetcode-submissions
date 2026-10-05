class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for token in strs:
            encoded_string += str(len(token)) + "#" + token
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+str_len])
            i += (j - i) + 1 + str_len
            
        return decoded_strs