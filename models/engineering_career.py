# Represents a <Category> career.
from models.career import Career

# Represents a Engineering career.

# Inherits from the Career base class.
class EngineeringCareer(Career):

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
        return f"{self.title} is an Engineering Career."