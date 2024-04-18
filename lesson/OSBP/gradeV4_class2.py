#git work plz

class Student:
    def __init__(self, student_id, name, english_score, code_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.code_score = code_score
        self.python_score = python_score
        self.total_score = self.english_score + self.code_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = None
        self.rank = None
 
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, search_key):
        for student in self.students:
            if student.student_id == search_key or student.name == search_key:
                self.students.remove(student)
                print(f"{student.name} 학생의 정보가 삭제되었습니다.")
                return True
        print("해당 학생을 찾을 수 없습니다.")
        return False

    def search_student(self, search_key):
        for student in self.students:
            if student.student_id == search_key or student.name == search_key:
                return student
        return None
    
    def output(self):
        print("====================================================================")
        print("학번    이름      영어   C언어    파이썬   총점    평균    학점   등수")
        print("====================================================================")
        for student in self.students:
            print(f"{student.student_id:<10} {student.name:<10} {student.english_score:<6} {student.code_score:<8} "
                f"{student.python_score:<9} {student.total_score:<6} {student.average_score:<8} {student.grade:<6} "
                f"{student.rank:<5}")
class GradeGet:
    @staticmethod
    def calculate_total_score(student):
        return student.english_score + student.code_score + student.python_score

    @staticmethod
    def calculate_average_score(student):
        return round(GradeGet.calculate_total_score(student) / 3, 2)
    
    @staticmethod
    def calculate_grade(student):
        average = GradeGet.calculate_average_score(student)
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
        
    @staticmethod
    def calculate_rank(students):
        ranked_students = sorted(students, key=lambda x: GradeGet.calculate_total_score(x), reverse=True)
        for i, student in enumerate(ranked_students):
            student.rank = i + 1

    @staticmethod
    def search_student_by_id(students, student_id):
        for student in students:
            if student.student_id == student_id:
                return student
        return None

    @staticmethod
    def search_student_by_name(students, name):
        for student in students:
            if student.name == name:
                return student
        return None

    @staticmethod
    def sort_by_total_score(students):
        students.sort(key=lambda x: GradeGet.calculate_total_score(x), reverse=True)

    @staticmethod
    def count_high_scores(students):
        count = sum(1 for student in students if GradeGet.calculate_total_score(student) >= 240)
        return count


def input_student_data():
    students = []
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        code_score = int(input("C-언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))

        student = Student(student_id, name, english_score, code_score, python_score)
        students.append(student)
    return students

def print_student_info(student):
    if student:
        print("검색 결과:")
        print(f"학번: {student.student_id}")
        print(f"이름: {student.name}")
        print(f"영어 점수: {student.english_score}")
        print(f"C언어 점수: {student.code_score}")
        print(f"파이썬 점수: {student.python_score}")
        print(f"총점: {student.total_score}")
        print(f"평균: {student.average_score}")
        print(f"학점: {student.grade}")
        print(f"등수: {student.rank}")
    else:
        print("해당 학생을 찾을 수 없습니다.")


def main():
    score_manager = StudentManager()
    students = input_student_data()
    for student in students:
        score_manager.add_student(student)
        student.grade = GradeGet.calculate_grade(student)

    GradeGet.calculate_rank(score_manager.students)
    score_manager.output()
    while True:
        action = input("작업 선택 (search,exit) : ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'search':
            search_key = input("검색할 학생의 학번 또는 이름 입력 : ")
            found_student = score_manager.search_student(search_key)
            print_student_info(found_student)
            if found_student:
                confirm = input("학생의 정보를 삭제(yes,no) : ")
                if confirm.lower() == 'yes':
                    score_manager.remove_student(found_student.student_id)

    

if __name__ == "__main__":
    main()
