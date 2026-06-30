from models.career import Career


class TechCareer(Career):

    def __init__(self, title, category, education_required, skills, interests):
        super().__init__(
            title,
            category,
            education_required,
            skills,
            interests
        )

    def get_description(self):
        return f"{self.title} is a Technology Career."