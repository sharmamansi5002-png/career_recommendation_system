# Base Career class used by all career categories.
class Career:
# Stores common career information.
    def __init__(self, title, category, education_required, skills, interests):
        self.title = title
        self.category = category
        self.education_required = education_required
        self.skills = skills
        self.interests = interests
# Initialize career attributes.
    def display_career(self):
        print(f"\nCareer: {self.title}")
        print(f"Category: {self.category}")
        print(f"Education Required: {self.education_required}")
# Display career information.
    def get_description(self):
        return f"{self.title} is a career in {self.category}"