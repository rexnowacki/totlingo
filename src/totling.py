
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
    def is_valid_name(self):
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
                print(f"Logged in as {child_name}.\n")
                return ChildProfile(child_name)
            else:
                print("Profile not found.\n")
                child_profile = Menu.main_menu()

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
        words = text.split()
        self.add_words_to_file(words)
        self.add_phrase_to_file(text)

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


class Menu:
    @staticmethod
    def main_menu():
        while True:
            print("Please select an option:")
            print("1. Create a New Profile")
            print("2. Login")
            print("3. Remove a Profile")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                child_profile = ChildProfile.create_new_profile()
                break
            elif choice == "2":
                child_profile = ChildProfile.login()
                break
            elif choice == "3":
                ChildProfile.remove_profile()
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
    def logged_in(child_profile):
        while True:
            print("Logged in menu:")
            print("1. Enter speech data")
            print("2. Go to analysis menu")
            print("3. Return to log-in")
            print("4. Quit")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                vocabulary_tracker = VocabularyTracker(child_profile)
                vocabulary_tracker.track_new_files()
                text = input("Enter a text string: ")
                vocabulary_tracker.process_text(text)
            elif choice == "2":
                if vocabulary_tracker is not None:
                    text_analyzer = TextAnalyzer(vocabulary_tracker.tracked_words_file)
                    text_analyzer.display_top_n_words()
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


