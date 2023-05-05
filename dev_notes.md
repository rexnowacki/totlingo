# TotLingo 

# childProfile.py
- Includes:
1. __init__:
  Creates directory for profile if it does not exist.
2. create_new_profile(): (static method)
  Gets input from user for "Child Name"
  Calls on ChildProfile to create dir if it does not exist.
  Displays success message.
3. remove_profile(): (static method)
  Removes profile directory and contents, user confirmed. 
4. login(): (static method)
  Checks for valid directory.
    If valid, advances to main menu.
    If invalid, displays error message.

# vocabTracker.py
- Includes:
1. __init__: 
  Gets child's name and valid directory name.
  Identifies phrases and words file location for writing. 
2. add_words_to_file(self, words):
  Reads tracked words file. Line by line, creates list of
    each word and its usage information. 
  If the word has been used before, it adds to the word count.
  If the word has not been used, sets count to 1. 
  Writes word to tracking file. 
3. add_phrase_to_file():
  Writes phrase as entered to phrases tracking file. 
4. process_text(self, text):
  Splits phrase into list of individual words. 
  Calls add_words_to_file.
  Calls add_phrase_to file.

# textAnalyzer.py
-Includes:
1. 
