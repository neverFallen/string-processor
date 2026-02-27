def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def word_count(text):
    if not text.strip():
        return 0
    return len(text.split())

def analyze_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return {
        "original": text,
        "reversed": reverse_string(text),
        "vowel_count": count_vowels(text),
        "word_count": word_count(text)
    }