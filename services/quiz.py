# ==========================================================
# Personality Quiz
#
# Collects the user's work style preferences to identify
# personality traits.
# ==========================================================

class PersonalityQuiz:
# Conducts a simple personality assessment.
    def start_quiz(self):

        print("\n--- Personality & Work Style Quiz ---")

        traits = []
# Ask questions and determine personality traits.
        q1 = input(
            "Do you prefer working with people or data? (people/data): "
        ).lower()

        if q1 == "people":
            traits.append("social")
        else:
            traits.append("analytical")

        q2 = input(
            "Do you enjoy creative tasks? (yes/no): "
        ).lower()

        if q2 == "yes":
            traits.append("creative")
        else:
            traits.append("practical")

        q3 = input(
            "Do you prefer structured or flexible environments? (structured/flexible): "
        ).lower()

        if q3 == "structured":
            traits.append("organized")
        else:
            traits.append("adaptive")
# Return the identified personality traits.
        return traits