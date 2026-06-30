class ReportGenerator:

    def generate(self, username, recommendations):

        with open("career_report.txt", "w") as file:

            file.write("CAREER RECOMMENDATION REPORT\n")
            file.write("=" * 40 + "\n\n")

            file.write(f"User: {username}\n\n")

            for career, score in recommendations:
                file.write(
                    f"{career.title} | "
                    f"{career.category} | "
                    f"Score: {score}\n"
                )

        print("Report exported successfully.")