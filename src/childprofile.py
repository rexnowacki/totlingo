import os
import shutil

"""The ChildProfile class represents a child's profile and provides functions
to create, remove, or log-in to a child's profile."""
class ChildProfile:
    def __init__(self, name):
        self.name = name.lower()
        # Creates a new directory with the child's name if it does not exist 
        if not os.path.exists(self.name):
            os.makedirs(self.name)

    # Static method to create a new child profile
    @staticmethod
    def create_new_profile():
        # Prompt the user for child's name
        child_name = input("Enter the child's name: ")
        # New ChildProfile object with the child's name
        child_profile = ChildProfile(child_name)
        print(f"Profile for {child_name} has been created.\n")
        return child_profile
    
    # Static method to remove existing profile
    @staticmethod
    def remove_profile():
        child_name = input("Enter the child's name for the profile to remove: ").lower()
        # Check if the profile directory exists
        if os.path.exists(child_name):
            # Give user a warning that the profile will be deleted
            confirm = input(f"Are you sure you want to delete the profile for {child_name}? (y/n): ").lower()
            # Remove profile directory via shutil 
            if confirm == 'y':
                shutil.rmtree(child_name)
                print(f"Profile for {child_name} has been removed.\n")
            else:
                print("Profile removal canceled.\n")
        else:
            print("Profile not found. Please try again.\n")
    
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
                print("Profile not found. Please try again.\n")

