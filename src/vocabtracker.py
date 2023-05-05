import os
import datetime

class VocabularyTracker:
    def __init__(self, child_profile):
        self.child_profile = child_profile
        self.tracked_words_file = f"{self.child_profile.name}/tracked_words.txt"
        self.tracked_phrases_file = f"{self.child_profile.name}/tracked_phrases.txt"


    def add_words_to_file(self, words):
        existing_words = {}

        if os.path.isfile(self.tracked_words_file):
            with open(self.tracked_words_file, "r") as file:
                for line in file:
                    word, count, first_date, last_date = line.strip().split(",")
                    existing_words[word] = (int(count), first_date, last_date)

        current_date = str(datetime.date.today())
        for word in words:
            if word in existing_words:
                count, first_date, _ = existing_words[word]
                existing_words[word] = (count + 1, first_date, current_date)
            else:
                existing_words[word] = (1, current_date, current_date)

        with open(self.tracked_words_file, "w") as file:
            for word, (count, first_date, last_date) in existing_words.items():
                file.write(f"{word},{count},{first_date},{last_date}\n")

    def add_phrase_to_file(self, phrase):
        current_date = str(datetime.date.today())

        with open(self.tracked_phrases_file, "a") as file:
            file.write(f"{phrase}|{current_date}\n")

    def process_text(self, text):
        words = text.split()
        self.add_words_to_file(words)
        self.add_phrase_to_file(text)
