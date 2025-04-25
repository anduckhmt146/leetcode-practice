from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            # Step 1: Determine how many words fit into the current line
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(w) for w in line_words)
            num_spaces = maxWidth - total_chars

            # Step 2: Build the line
            # Build last line
            if j == len(words) or num_words == 1:
                # Last line or single word -> left justified
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            # Build middle line
            else:
                # Fully justify
                spaces_between = num_words - 1
                space, extra = divmod(num_spaces, spaces_between)
                line = ''
                for k in range(spaces_between):
                    line += line_words[k]
                    line += ' ' * (space + (1 if k < extra else 0))
                line += line_words[-1]  # Last word

            res.append(line)
            i = j
        return res
