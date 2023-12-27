student_scores = {
    "Ufuk": 81,
    "Hasan": 78,
    "Mustafa": 95,
    "Polat": 53,
    "Cengiz": 62,
}

student_grades = {}


def grade_editor():
    for _ in student_scores:
        student_grades[_] = student_scores[_]


grade_editor()
print(list(student_grades.items()))
