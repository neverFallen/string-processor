def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count = count + 1
    return count


def word_count(text):
    if text.strip() == "":
        return 0
    words = text.split()
    return len(words)


def analyze_text(text):
    result = {
        "original": text,
        "reversed": reverse_string(text),
        "vowel_count": count_vowels(text),
        "word_count": word_count(text)
    }
    return result

if __name__ == "__main__":
    print("=== Simple String Analyzer ===")
    print("Type some text (or type 'quit' to stop)")
    print("----------------------------------")
    
    while True:
        text = input("Your text: ").strip()
        
        if text.lower() == "quit":
            print("Goodbye!")
            break
            
        if text == "":
            print("You typed nothing. Try again.\n")
            continue
            
        result = analyze_text(text)
        
        print("\nResult:")
        print("Original :", result["original"])
        print("Reversed :", result["reversed"])
        print("Vowels   :", result["vowel_count"])
        print("Words    :", result["word_count"])
        print("----------------------------------\n")