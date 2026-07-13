# Represents a <Category> career.
from models.career import Career
# Represents a Creative career.

# Inherits from the Career base class.
class CreativeCareer(Career):

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
        return f"{self.title} is a Creative Career."