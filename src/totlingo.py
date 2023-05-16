
import os
import shutil
import datetime
import string

"""The ChildProfile class represents a child's profile and provides functions
to create, remove, or log-in to a child's profile."""
class ChildProfile:
    def __init__(self, name):
        # Make sure name is valid
        if not self.is_valid_name(name):
            raise ValueError("Invalid name.")
        self.name = name.lower()
        # Creates a new directory with the child's name if it does not exist 
        if not os.path.exists(self.name):
            os.makedirs(self.name)
    
    # Static method to validate name
    @staticmethod
    def is_valid_name(name):
        # Name must be non-empty and can only contain alphanumerics
        return bool(name) and name.isalpha()

    # Static method to create a new child profile
    @staticmethod
    def create_new_profile():
        # Prompt the user for child's name
        child_name = input("Enter the child's name: ")
        # Check if name is valid and profile doesn't already exist 
        if ChildProfile.is_valid_name(child_name) and not os.path.exists(child_name.lower()):
            child_profile = ChildProfile(child_name)
            print(f"Profile for {child_name.capitalize()} has been created.\n")
            return child_profile
        else:
            print("Invalid name or profile already exists. Please try again.")
    
    # Static method to remove existing profile
    @staticmethod
    def remove_profile():
        child_name = input("Enter the child's name for the profile to remove: ").lower()
        # Check if the profile directory exists
        if os.path.exists(child_name):
            # Give user a warning that the profile will be deleted
            confirm = input(f"Are you sure you want to delete the profile for {child_name.capitalize()}? (y/n): ").lower()
            # Remove profile directory via shutil 
            if confirm == 'y':
                shutil.rmtree(child_name)
                print(f"Profile for {child_name.capitalize()} has been removed.\n")
            else:
                print("Profile removal canceled.\n")
        else:
            print("Profile not found.\n")
            child_profile = Menu.main_menu()
    
    # Static method to log in to an existing profile
    @staticmethod
    def login():
        while True:
            child_name = input("Enter the child's name for the profile: ").lower()
            # Verify that profile directory exists and return profile/directory name
            if os.path.exists(child_name):
                print(f"Logged in as {child_name.capitalize()}.\n")
                return ChildProfile(child_name)
            else:
                print("Profile not found.\n")
                return None
                # child_profile = Menu.main_menu()

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
                    existing_words[word.lower()] = (int(count), first_date, last_date)

        current_date = str(datetime.date.today())
        for word in words:
            word = word.lower() # convert word to lowercase
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

    def track_new_files(self):
        directory = self.child_profile.name
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename not in {"tracked_words.txt", "tracked_phrases.txt"}:
                filepath = os.path.join(directory, filename)
                with open(filepath, "r") as file:
                    text = file.read()
                if input(f"Do you want to track words from {filename}? (y/n): ").lower() == 'y':
                    self.process_text(text)
                    print(f"Tracked words from {filename}.")
                    os.remove(filepath)  # delete the file
                    print(f"Deleted {filename}.")

    def process_text(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.lower().split()
        self.add_words_to_file(words)
        self.add_phrase_to_file(text)

class TextAnalyzer:
    def __init__(self, tracked_words_file):
        self.tracked_words_file = tracked_words_file
        self.stop_words = self.read_stop_words()

    def read_stop_words(self):
        with open('stop_words.txt', 'r') as f:
            return set(word.strip() for word in f.read().split(','))

    def get_word_counts(self):
        word_counts = {}

        if os.path.isfile(self.tracked_words_file):
            with open(self.tracked_words_file, "r") as file:
                for line in file:
                    word, count, first_date, last_date = line.strip().split(",")
                    # if word not in self.stop_words: <--- Uncomment if don't want to count stop words
                    word_counts[word] = int(count)

        return word_counts

    def top_n_words(self, n=30):
        word_counts = self.get_word_counts()
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_word_counts[:n]

    def display_top_n_words(self, n=30):
        top_words = self.top_n_words(n)
        print(f"Top {n} words with the highest counts:")
        for i, (word, count) in enumerate(top_words, start=1):
            print(f"{i}. {word} - {count}")

    def word_usage_ratio(self):
        word_counts = self.get_word_counts()
        word = input("Enter word to get word usage data: ").lower()

        if word not in word_counts:
            print(f"The word '{word}' has not been used.")
            return 0
        total_words = sum(word_counts.values())
        word_count = word_counts[word]
        usage_ratio = word_count / total_words
        
        print(f"The word '{word}' has been used {word_count} times.")
        print(f"Total number of words used is {total_words}.")
        print(f"The usage ratio of the word '{word}' is {usage_ratio:.2%}.")
        
        return usage_ratio
    
    def count_unique_words(self):
        word_counts = self.get_word_counts()
        unique_words = len(word_counts)
        print(f"The total number of unique words is {unique_words}.")
        return unique_words
    
    def longest_words(self, n=15):
        word_counts = self.get_word_counts()
        sorted_words = sorted(word_counts.keys(), key=len, reverse=True)
        longest_words = sorted_words[:n]

        print(f"The {n} longest words are:")
        for i, word in enumerate(longest_words, start=1):
            print(f"{i}. {word} - {len(word)} characters")
        return longest_words


class Menu:
    @staticmethod
    def main_menu():
        while True:
            print("Please select an option:")
            print("1. Create a New Profile")
            print("2. Login")
            print("3. Remove a Profile")
            print("4. Quit")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                child_profile = ChildProfile.create_new_profile()
                break
            elif choice == "2":
                child_profile = ChildProfile.login()
                break
            elif choice == "3":
                ChildProfile.remove_profile()
            elif choice == "4":
                exit()
            else:
                print("Invalid choice. Please try again.\n")
        return child_profile

    @staticmethod
    def logout_menu():
        while True:
            print("Logout menu:")
            print("1. Go to main menu")
            print("2. Exit")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                print("Invalid choice. Please try again.\n")

    @staticmethod
    def analysis_menu(text_analyzer):
       while True:
            print("Analysis menu:")
            print("1. Longest Words")
            print("2. Word Usage Ratio")
            print("3. Count Unique Words")
            print("4. Display Top Words")
            print("5. Return to Previous Menu")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                text_analyzer.longest_words()
            elif choice == "2":
                text_analyzer.word_usage_ratio()
            elif choice == "3":
                text_analyzer.count_unique_words()
            elif choice == "4":
                text_analyzer.display_top_n_words()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.\n")

    def speech_entry(vocabulary_tracker):
        while True:
            print("Speech Entry menu:")
            print("1. Enter Speech Data")
            print("2. Return to Previous Menu")
            choice = input("Enter the number of your chouce: ")

            if choice == "1":
                text = input("Enter a text string to parse: ")
                vocabulary_tracker.process_text(text)
                print("Files updated.")
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please try again.\n")
    
    @staticmethod
    def logged_in(child_profile):
        while True:
            print("Logged in menu:")
            print("1. Enter speech data")
            print("2. Analysis menu")
            print("3. Return to log-in")
            print("4. Quit")
            choice = input("Enter the number of your choice: ")
            vocabulary_tracker = VocabularyTracker(child_profile)
            if choice == "1":
                vocabulary_tracker.track_new_files()
                Menu.speech_entry(vocabulary_tracker)
            elif choice == "2":
                if vocabulary_tracker is not None:
                    text_analyzer = TextAnalyzer(vocabulary_tracker.tracked_words_file)
                    Menu.analysis_menu(text_analyzer)             
                else:
                    print("No speech data entered yet.")
            elif choice == "3":
                break
            elif choice == "4":
                exit()
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    while True:
        child_profile = Menu.main_menu()

        if child_profile:
            Menu.logged_in(child_profile)


