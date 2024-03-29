# -*- coding: utf-8 -*-
"""pas pirozi3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qt0zWLynijRTQlRo4TJQofSyQeHqmsqW
"""

import re

class TextProcessor:
    def __init__(self, text):
        self.text = self._clean_text(text)
        self.words = self.text.split(" ")

    def _clean_text(self, text):
        return re.sub(r'[،:؛.؟!٬٫]+', '', text)

    def _get_word_distance(self, word1, word2):
        if len(word1) < len(word2):
            word1 += '_' * (len(word2) - len(word1))
        elif len(word1) > len(word2):
            word2 += '_' * (len(word1) - len(word2))

        return sum(char1 != char2 for char1, char2 in zip(word1, word2))

    def get_similar_words(self, reference_word, max_distance):
        return [word for word in self.words if self._get_word_distance(word, reference_word) <= max_distance]


max_distance = int(input())
text = input()
reference_word = input()

processor = TextProcessor(text)
similar_words = processor.get_similar_words(reference_word, max_distance)

print("\n".join(similar_words))