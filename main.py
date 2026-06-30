from services.auth import AuthService
from services.quiz import PersonalityQuiz
from services.recommendation_engine import RecommendationEngine
from services.report_generator import ReportGenerator

from database.setup import create_tables
from database.career_repository import CareerRepository

create_tables()

auth = AuthService()

print("1. Register")
print("2. Login")

choice = input("Choose an option: ")

if choice == "1":
    current_user = auth.register()
else:
    current_user = auth.login()

if current_user:

    quiz = PersonalityQuiz()

    traits = quiz.start_quiz()

    print("\nYour personality traits:", traits)

    engine = RecommendationEngine()

    recommendations = engine.recommend(current_user, traits)

    print("\nTop Career Recommendations:\n")

    repo = CareerRepository()

    for career, score in recommendations:

        print(
            f"- {career.title} "
            f"({career.category}) "
            f"(Score: {score})"
        )

        print(career.get_description())

        repo.save_recommendation(
            current_user["username"],
            career.title,
            score
        )

    report = ReportGenerator()

    report.generate(
        current_user["username"],
        recommendations
    )