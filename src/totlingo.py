
import os
import datetime
import shutil



class ChildProfile:
    def __init__(self, name, birth_date):
        self.name = name.lower()
        self.birth_date = birth_date

        if not os.path.exists(self.name):
            os.makedirs(self.name)

    @staticmethod
    def create_new_profile():
        child_name = input("Enter the child's name: ")
        birth_date = input("Enter the child's birth date (YYYY-MM-DD): ")
        child_profile = ChildProfile(child_name, birth_date)
        print(f"Profile for {child_name} has been created.\n")
        return child_profile
    
    @staticmethod
    def remove_profile():
        child_name = input("Enter the child's name for the profile to remove: ").lower()
        if os.path.exists(child_name):
            confirm = input(f"Are you sure you want to delete the profile for {child_name}? (y/n): ").lower()
            if confirm == 'y':
                shutil.rmtree(child_name)
                print(f"Profile for {child_name} has been removed.\n")
            else:
                print("Profile removal canceled.\n")
        else:
            print("Profile not found. Please try again.\n")

    @staticmethod
    def login():
        while True:
            child_name = input("Enter the child's name for the profile: ").lower()
            if os.path.exists(child_name):
                print(f"Logged in as {child_name}.\n")
                return ChildProfile(child_name, None)
            else:
                print("Profile not found. Please try again.\n")

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

if __name__ == "__main__":
    child_profile = main_menu()
    

    if child_profile:
        text = input("Enter a text string: ")
        vocabulary_tracker = VocabularyTracker(child_profile)
        vocabulary_tracker.process_text(text)
