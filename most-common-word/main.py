from collections import defaultdict
import string

def most_common_word(paragraph, banned) -> str:
    word_dict = defaultdict(int)
    paragraph_array = paragraph.split(" ")
    exclude = set(string.punctuation)

    for word in paragraph_array:
        word = ''.join(ch for ch in word if ch not in exclude).lower()
        if word not in banned:
            word_dict[word] += 1

    return max(word_dict, key = word_dict.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph, banned))
