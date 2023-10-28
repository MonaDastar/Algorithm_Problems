def process_student_scores(scores):
    for student in scores:
        match student:
            case(name, "math", score) if isinstance(score, int) and score >= 90:
                print(f" {name} excelled in math with the score of {score}.")
            case(name,subject,score) if isinstance(score, int) and score >= 70:
                print(f"{student} performed well in {subject} with a score of {score}.")
            case (name,subject,score):
                print(f"{student} needs to practice more in {subject} with the score of {score}.")
            case _:
                print("Invalid data for a student.")
                
        
        
# Example usage:
student_scores = [
    ("Mona", "Math", 95),
    ("Ashkan", "Science", 80),
    ("Zari", "History", 65),
    ("Bob", "English", 75),
    ("Ava", "Math", 60),
    ("Darya", "Physics", "Invalid")
]

process_student_scores(student_scores)