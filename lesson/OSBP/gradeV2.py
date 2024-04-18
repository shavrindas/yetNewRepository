


# Initialize empty lists to store student names and their scores
student_names = []
english_scores = []
code_scores = []
math_scores = []
total_scores = []

# Ask for student names and their scores for 5 times
i = 0 
while i < 5:
    name = input("이름 : ")
    english_score = input("영어 점수 : ")
    code_score = input("코딩 점수 : ")
    math_score = input("수학 점수 : ")

    # If user types 're', remove the last student's data and continue with the current student
    if english_score == 're' or code_score == 're' or math_score == 're':
        if i != 0:
            student_names.pop()
            english_scores.pop()
            code_scores.pop()
            math_scores.pop()
            i -= 1
        continue

    # Validate the scores
    if not(0 <= int(english_score) <= 100) or not(0 <= int(code_score) <= 100) or not(0 <= int(math_score) <= 100):
        print("점수는 0에서 100 사이의 값이어야 합니다. 다시 입력해주세요.")
        continue

    # Store the inputs into the respective lists
    student_names.append(name)
    english_scores.append(int(english_score))
    code_scores.append(int(code_score))
    math_scores.append(int(math_score))
    i += 1

# Calculate total scores, averages, and grades for each student
average_scores = []
grades = []

for i in range(5):
    total_score = english_scores[i] + code_scores[i] + math_scores[i]
    total_scores.append(total_score)  # Store each student's total score
    average_score = total_score / 3
    average_scores.append(average_score)

    # Assign grades
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    grades.append(grade)

# Rank students based on average scores
ranks = sorted(range(len(average_scores)), key=lambda x: average_scores[x], reverse=True)
ranks = [ranks.index(i)+1 for i in range(len(ranks))]

# Print student name, total score, average score, grade, and rank
for i in range(5):
    print(f"이름 : {student_names[i]:<10} 학점 : {grades[i]:<2} 순위 : {ranks[i]:<2}")
    print(f"총점 : {total_scores[i]:<3} 평균 : {format(average_scores[i], '.2f'):<5}")  # Use total_scores[i] instead of total_score[i]