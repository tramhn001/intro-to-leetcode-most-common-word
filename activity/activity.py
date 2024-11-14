# Notice the naming is a bit off from typical Python. This is pretty common
# in Leetcode. Don't let this affect writing good PEP8-style python in your own
# code.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Filter out punctuation
        filtered_paragraph = "".join([c if c.isalpha() or c.isspace else " " for c in paragraph])

        # get words from paragraph
        words = filtered_paragraph.split()

        # filter out a word if it is banned
        banned_set = set(banned)
        valid_words = [word for word in words if word not in banned_set]

        # count each word occurence 
        counts = {}
        for word in valid_words:
            counts[word] = counts.get(word, 0) + 1
        # find the word with the highest count:

        max_word = max(counts, key=counts.get)

        # Return the word:
        return max_word