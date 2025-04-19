class Solution:
    def reverseVowels(self, s: str) -> str:
        # Give all the vowels first
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelWord = []
        for character in s:
            if character.lower() in vowels:
                vowelWord.append(character)

        right = len(vowelWord) - 1
        s_list = list(s)
        for i in range(0, len(s_list)):
            if s[i].lower() in vowels:
                s_list[i] = vowelWord[right]
                right -= 1

        return ''.join(s_list)

        