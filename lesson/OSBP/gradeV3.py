#입력 함수 
def input_data():
    student = []
    for i in range(5):
        student.append([])
        student[i].append(input("학번: "))
        student[i].append(input("이름: "))
        student[i].append(int(input("영어: ")))
        student[i].append(int(input("C언어: ")))
        student[i].append(int(input("파이썬: ")))
    return student

def count_high_scores(student):
    count = 0
    for i in range(len(student)):
        if student[i][6] >= 80:
            count += 1
    return count

def sum_avg(student):
    for i in range(len(student)):
        student[i].append(student[i][2] + student[i][3] + student[i][4])
        student[i].append(round(student[i][5] / 3, 2))  # 평균을 실수로 계산
        if student[i][6] >= 90:
            student[i].append('A')
        elif student[i][6] >= 80:
            student[i].append('B')
        elif student[i][6] >= 70:
            student[i].append('C')
        elif student[i][6] >= 60:
            student[i].append('D')
        else:
            student[i].append('F')
    return student

def rank(student):
    student.sort(key=lambda x: x[6], reverse=True)  # 평균 점수를 기준으로 내림차순 정렬
    for i in range(len(student)):
        if i > 0 and student[i][6] == student[i-1][6]:  # 이전 학생과 평균 점수가 같다면 같은 등수
            student[i].append(student[i-1][7])
        else:  # 이전 학생과 평균 점수가 다르다면 현재 순서(0부터 시작하므로 1을 더함)가 등수
            student[i].append(i+1)
    return student

def output(student):
    print("==============================================")
    print("학번 이름 영어 C언어 파이썬 총점 평균 학점 등수")
    print("==============================================")
    for i in range(len(student)):
        print(student[i][0], student[i][1], student[i][2], student[i][3], student[i][4], student[i][5], student[i][6], student[i][7], student[i][8])

def main():
    student = []
    student = input_data()
    student = sum_avg(student)
    student = rank(student)
    output(student)
    high_score_count = count_high_scores(student)
    print("80점 이상 학생 수: ", high_score_count)

main()