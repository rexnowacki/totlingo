
from childprofile import ChildProfile
from vocabtracker import VocabularyTracker
from textanalyzer import TextAnalyzer
from menu import Menu
    
if __name__ == "__main__":
    while True:
        child_profile = Menu.main_menu()

        if child_profile:
            Menu.logged_in(child_profile)
"""
            while True:
                choice = Menu.logged_in()
            
            text = input("Enter a text string: ")
            vocabulary_tracker = VocabularyTracker(child_profile)
            vocabulary_tracker.process_text(text)

            text_analyzer = TextAnalyzer(vocabulary_tracker.tracked_words_file)
            text_analyzer.display_top_n_words()

            if not Menu.logout_menu():
                break
"""
