class Student:
    def __init__(self, student_id, name, english_score, code_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.code_score = code_score
        self.python_score = python_score
        self.total_score = self.english_score + self.code_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


class ScoreManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)

    def calculate_rank(self):
        ranked_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(ranked_students):
            student.rank = i + 1

    def print_scores(self):
        for student in self.students:
            print(f"학번: {student.student_id}, 이름: {student.name}, 총점: {student.total_score}, "
                  f"평균: {student.average_score}, 학점: {student.grade}, 순위: {student.rank}")


def main():
    score_manager = ScoreManager()
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        code_score = int(input("C-언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))

        student = Student(student_id, name, english_score, code_score, python_score)
        score_manager.add_student(student)

    score_manager.calculate_rank()
    score_manager.print_scores()


if __name__ == "__main__":
    main()




'''


새로운 요구사항
성적관리프로그램 (객체지향 프로그램으로 수정하기)

 조건: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 

         키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램 작성

       - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 

       - 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수 




'''