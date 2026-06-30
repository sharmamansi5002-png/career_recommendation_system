from models.career import Career


class EngineeringCareer(Career):

    def __init__(self, title, category, education_required, skills, interests):
        super().__init__(
            title,
            category,
            education_required,
            skills,
            interests
        )

    def get_description(self):
        return f"{self.title} is an Engineering Career."