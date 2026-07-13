# Represents a <Category> career.
from models.career import Career

# Represents a Business career.
# Inherits from the Career base class.
class BusinessCareer(Career):

    def __init__(self, title, category, education_required, skills, interests):
        super().__init__(
            title,
            category,
            education_required,
            skills,
            interests
        )
# Display category-specific career information.
    def get_description(self):
        return f"{self.title} is a Business Career."