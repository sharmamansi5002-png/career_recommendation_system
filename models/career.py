class Career:
    def __init__(self, title, category, education_required, skills, interests):
        self.title = title
        self.category = category
        self.education_required = education_required
        self.skills = skills
        self.interests = interests

    def display_career(self):
        print(f"\nCareer: {self.title}")
        print(f"Category: {self.category}")
        print(f"Education Required: {self.education_required}")