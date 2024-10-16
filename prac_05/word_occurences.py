"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

def main():
    input_words = input("Input your text: ").split()
    words_counter = {}

    for word in input_words:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    sorted_words_counter = dict(sorted(words_counter.items()))
    longest_word = max(len(word) for word in words_counter.keys())

    for word, count in sorted_words_counter.items():
        print(f"{word:{longest_word}} : {count}")

main()
