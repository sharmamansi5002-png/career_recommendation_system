import json

from models.tech_career import TechCareer
from models.business_career import BusinessCareer
from models.medical_career import MedicalCareer
from models.engineering_career import EngineeringCareer
from models.creative_career import CreativeCareer


class RecommendationEngine:

    def load_careers(self):

        with open("data/careers.json", "r") as file:
            data = json.load(file)

        careers = []

        for item in data:

            category = item["category"]

            if category == "Technology":
                career = TechCareer(
                    item["title"],
                    category,
                    item["education_required"],
                    item["skills"],
                    item["interests"]
                )

            elif category == "Business":
                career = BusinessCareer(
                    item["title"],
                    category,
                    item["education_required"],
                    item["skills"],
                    item["interests"]
                )

            elif category == "Medical":
                career = MedicalCareer(
                    item["title"],
                    category,
                    item["education_required"],
                    item["skills"],
                    item["interests"]
                )

            elif category == "Engineering":
                career = EngineeringCareer(
                    item["title"],
                    category,
                    item["education_required"],
                    item["skills"],
                    item["interests"]
                )

            else:
                career = CreativeCareer(
                    item["title"],
                    category,
                    item["education_required"],
                    item["skills"],
                    item["interests"]
                )

            careers.append(career)

        return careers

    def calculate_match(self, user, career, personality):

        score = 0

        # Skill Match (10 points each)
        for skill in user["skills"]:
            for required in career.skills:
                if skill.strip().lower() == required.strip().lower():
                    score += 10

        # Interest Match (8 points each)
        for interest in user["interests"]:
            for required in career.interests:
                if interest.strip().lower() == required.strip().lower():
                    score += 8

        # Personality Match
        personality_text = " ".join(personality).lower()

        if career.category == "Technology":
            if "analytical" in personality_text:
                score += 8

        elif career.category == "Creative":
            if "creative" in personality_text:
                score += 8

        elif career.category == "Business":
            if "social" in personality_text:
                score += 8

        elif career.category == "Medical":
            if "social" in personality_text:
                score += 8

        elif career.category == "Engineering":
            if "organized" in personality_text:
                score += 8

        # Education Match
        if career.education_required == "Bachelor's":
            score += 5

        return score

    def recommend(self, user, personality):

        careers = self.load_careers()

        results = []

        for career in careers:

            score = self.calculate_match(
                user,
                career,
                personality
            )

            results.append((career, score))

        results.sort(key=lambda x: x[1], reverse=True)

        return results[:5]