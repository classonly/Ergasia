import math

class StudentScores:
    def __init__(self, students_scores):
        self.students_scores = students_scores

    def calculate_averages(self):
        subjects = {'Math': 0, 'Physics': 0, 'English': 0}

        for student in self.students_scores:
            subjects['Math'] += student[1]
            subjects['Physics'] += student[2]
            subjects['English'] += student[3]

        num_students = len(self.students_scores)

        return {subject: (total / num_students) for subject, total in subjects.items()}

    def top_students(self):
        top_scores = {'Math': ('', 0), 'Physics': ('', 0), 'English': ('', 0)}

        for student in self.students_scores:
            name, math, physics, english = student

            if math > top_scores['Math'][1]:
                top_scores['Math'] = (name, math)
            if physics > top_scores['Physics'][1]:
                top_scores['Physics'] = (name, physics)
            if english > top_scores['English'][1]:
                top_scores['English'] = (name, english)

        return {subject: student[0] for subject, student in top_scores.items()}

    def students_above_threshold(self, threshold):
        count = 0
        for student in self.students_scores:
            name, math, physics, english = student
            if math > threshold and physics > threshold and english > threshold:
                count += 1

        return count

    def unique_scores(self):
        unique_set = set()

        for student in self.students_scores:
            name, math, physics, english = student
            unique_set.update([math, physics, english])

        return unique_set

    def calculate_std_deviation(self):
        subjects = {'Math': [], 'Physics': [], 'English': []}

        for student in self.students_scores:
            subjects['Math'].append(student[1])
            subjects['Physics'].append(student[2])
            subjects['English'].append(student[3])

        std_deviation = {}
        for subject, scores in subjects.items():
            mean = sum(scores) / len(scores)
            variance = sum((x - mean) ** 2 for x in scores) / len(scores)
            std_deviation[subject] = round(math.sqrt(variance), 2)

        return std_deviation



students_scores = [
    ('Alice', 85, 90, 82),
    ('Bob', 78, 76, 88),
    ('Charlie', 92, 89, 95),
    ('David', 70, 72, 68),
    ('Eve', 88, 92, 91)
]

scores = StudentScores(students_scores)


print("Averages:", scores.calculate_averages())


print("Top Students:", scores.top_students())


threshold = 80
print(f"Students above threshold ({threshold}):", scores.students_above_threshold(threshold))


print("Unique Scores:", scores.unique_scores())


print("Standard Deviations:", scores.calculate_std_deviation())
