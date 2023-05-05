from childprofile import ChildProfile
from vocabtracker import VocabularyTracker
from textanalyzer import TextAnalyzer
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
                text = input("Enter a text string: ")
                vocabulary_tracker = VocabularyTracker(child_profile)
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

