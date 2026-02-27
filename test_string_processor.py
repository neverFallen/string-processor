import unittest
from string_processor import reverse_string, count_vowels, word_count, analyze_text

class TestStringProcessor(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("123!@#"), "#@!321")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("queue"), 4)

    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)
        self.assertEqual(word_count("one two three"), 3)
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("   "), 0)
        self.assertEqual(word_count("python is great!"), 3)

    def test_analyze_text(self):
        text = "Hi there everyone"
        result = analyze_text(text)
        self.assertEqual(result["original"], "Hi there everyone")
        self.assertEqual(result["reversed"], "enoyreve ereht iH")
        self.assertEqual(result["word_count"], 3)
        self.assertEqual(result["vowel_count"], 7)

    def test_analyze_text_empty(self):
        result = analyze_text("")
        self.assertEqual(result["word_count"], 0)
        self.assertEqual(result["vowel_count"], 0)
        self.assertEqual(result["reversed"], "")

if __name__ == "__main__":
    unittest.main()