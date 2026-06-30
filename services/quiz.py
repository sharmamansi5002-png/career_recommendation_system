class PersonalityQuiz:
    def start_quiz(self):
        print("\n--- Personality & Work Style Quiz ---")

        q1 = input("Do you prefer working with people or data? (people/data): ").strip().lower()
        q2 = input("Do you enjoy creative tasks? (yes/no): ").strip().lower()
        q3 = input("Do you prefer structured or flexible environments? (structured/flexible): ").strip().lower()

        personality = []

        if q1 == "people":
            personality.append("social")
        else:
            personality.append("analytical")

        if q2 == "yes":
            personality.append("creative")
        else:
            personality.append("practical")

        if q3 == "structured":
            personality.append("organized")
        else:
            personality.append("adaptive")

        return personality
