class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            word = word.split(ch, 1)
            word[0] = "".join(reversed(word[0]))
            return ch + word[0] + word[1]
        else:
            return word