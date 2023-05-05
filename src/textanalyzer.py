import os

class TextAnalyzer:
    def __init__(self, tracked_words_file):
        self.tracked_words_file = tracked_words_file

    def get_word_counts(self):
        word_counts = {}

        if os.path.isfile(self.tracked_words_file):
            with open(self.tracked_words_file, "r") as file:
                for line in file:
                    word, count, first_date, last_date = line.strip().split(",")
                    word_counts[word] = int(count)

        return word_counts

    def top_n_words(self, n=10):
        word_counts = self.get_word_counts()
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_word_counts[:n]

    def display_top_n_words(self, n=10):
        top_words = self.top_n_words(n)
        print(f"Top {n} words with the highest counts:")
        for i, (word, count) in enumerate(top_words, start=1):
            print(f"{i}. {word} - {count}")
