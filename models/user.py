class User:
    def __init__(self, name, age, education, skills, interests):
        self.name = name
        self.age = age
        self.education = education
        self.skills = skills
        self.interests = interests

    def display_profile(self):
        print("\n===== USER PROFILE =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Education: {self.education}")
        print(f"Skills: {', '.join(self.skills)}")
        print(f"Interests: {', '.join(self.interests)}")
