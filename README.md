
# Child Vocabulary Tracker and Analyzer

This program is designed to track and analyze the vocabulary of a child over time. It allows 
users to create, remove, and log into child profiles, and then input, store, and analyze 
vocabulary data for each profile. The program includes several analysis functions, such as 
displaying the most frequently used words, calculating word usage ratio, counting unique words, 
and finding the longest words.

## Configuration Instructions

This program is written in Python and requires Python 3.x to run. Make sure you have the 
correct version of Python installed on your system. 

## Installation Instructions

No specific installation is required. Download the Python file and run it in your Python 
environment.

## Operating Instructions

1. Run the Python file. The main menu will appear.
2. Choose to create a new profile, log in, remove a profile, or quit the program.
3. If you log in, you can enter speech data, go to the analysis menu, return to log-in, or 
quit the program.
4. In the analysis menu, you can view the longest words, calculate word usage ratio, count 
unique words, display top words, or return to the previous menu.
5. If you would prefer to add words to the vocabulary tracking file by the program parsing
a text file, place a text file in the sub-directory of a valid child profile. 

## File Manifest

- child_vocabulary_tracker.py
- stop_words.txt (this file should contain a comma-separated list of stop words)

## Contact Information

For any inquiries or support, please contact me at [cnowacki@mail.pima.edu].

## Known Bugs

No known bugs as of the latest update.

## Troubleshooting

If you encounter any issues, please try the following:
1. Ensure that you are using the correct version of Python (3.x).
2. Check that you have the 'stop_words.txt' file in the same directory as the Python file.
3. If you're still experiencing issues, please contact me at [cnowacki@mail.pima.edu].

## Credits and Acknowledgments

This project was developed by [Christopher Nowacki].

## Feature Requests
1. Implement date-based analysis. 

## Changelog

[05/14/2023: Added file tracking capabilities. If you place a plain text file in the directory
            of a valid profile, when you go to enter speech data the program will ask you if 
            you would like the .txt file scanned into vocabulary data.]

