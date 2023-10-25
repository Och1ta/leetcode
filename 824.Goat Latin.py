class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        temp_list = []
        vowels = set("aeiou")
        count = 1

        for i in sentence.split(' '):

            if i[0].lower() in vowels:
                i += 'ma'

            else:
                i = i[1:] + i[0] + "ma"

            i = i + 'a' * count
            count += 1
            temp_list.append(i)
        return ' '.join(temp_list)