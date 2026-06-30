from models.career import Career


class BusinessCareer(Career):

    def __init__(self, title, category, education_required, skills, interests):
        super().__init__(
            title,
            category,
            education_required,
            skills,
            interests
        )

    def get_description(self):
        return f"{self.title} is a Business Career."