# ==========================================================
# Authentication Service
#
# Handles user registration and login using a JSON file.
# ==========================================================

import json
import os

USERS_FILE = "data/user_profiles.json"

# Provides user authentication features.

class AuthService:
# Register a new user and save the profile.

    def register(self):
        username = input("Username: ")
        email = input("Email: ")

        skills = input("Skills (comma separated): ").split(",")
        interests = input("Interests (comma separated): ").split(",")
# Store user information in dictionary format.
        user = {
            "username": username,
            "email": email,
            "skills": [s.strip() for s in skills],
            "interests": [i.strip() for i in interests]
        }
# Load existing users from the JSON file.
        users = []

        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                try:
                    users = json.load(file)
                except:
                    users = []

        if not isinstance(users, list):
            users = []
# Add the new user to the list.
        users.append(user)

        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)

        print("Registration successful")

        return user
# Save the updated user list.
    def login(self):
        username = input("Username: ")

        if not os.path.exists(USERS_FILE):
            print("No users found")
            return None

        with open(USERS_FILE, "r") as file:
            users = json.load(file)
# Authenticate an existing user.
        for user in users:
            if user["username"] == username:
                print("Login successful")
                return user

        print("User not found")
        return None