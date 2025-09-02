#!/usr/bin/env python
import sys
import csv


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {} #dict로 저장

    with open(filepath, 'r', encoding='utf-8') as f: #filepath를 열고 utf-8로 인코딩한다
        csv_reader = csv.reader(f) #한줄씩 출력 ex) ["이름","국어","수학","영어","과학","사회"], ...

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:] #row[0]는 이름 row[1:]은 이름 이후의 모든 열들을 딕셔너리로 출력
    return student_scores, header[1:] # 딕셔너리와, 과목명 리스트("이름" 제외)를 반환


def subject_average(student_scores: dict, subjects: list):
    '''
    sums = [0.0]*len(subjects) # 과목별 합계 리스트 [0, 0, 0, ...]
    for score in student_scores.values(): # 학생별 모든 과목 점수를 리스트형태로 출력 
        for i, s in enumerate(score): # 리스트 점수들을 idx와 함께 차례대로 출력
            sums[i] += float(s) # sums 리스트에 idx(과목의 자릿수) 별 점수가 누적 합계된다.
    n = len(student_scores) # 학생 인원
    return {subjects[i] : round(sums[i] / n, 1) for i in range(len(subject))} #딕셔너리로 과목 : 평균값을 만든다.
    '''
    rows = [list(map(float, score)) for score in student_scores.values()] # 학생들의 점수들을 실수화하여 리스트로 정리 ex) [(학생A 점수들), (학생B 점수들)...]
    cols = list(zip(*rows)) # 과목별 점수들을 리스트로 정리, 행 리스트가 하나가 아닌 여러개이므로 *를 붙여야한다. ex) [(국어점수들), (수학점수들)...]
    n = len(rows) #학생 인원
    return {sub : round(sum(col) / n, 1) for sub, col in zip(subjects, cols)} #[과목, 과목 점수 함계] = [sub, cols]로 바꿔 과목 : 평균값을 차례대로 나열



    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """


def student_average(student_scores: dict):
    ave = ((n, round(sum(map(float, s)) / len(s), 1)) for n, s in student_scores.items()) #학생이름과 그 학생의 점수들을 실수로 바꿔 다 합친 다음 점수 갯수로 나누어 이름, 평균값인 튜플로 나타냄
    return sorted(ave, key = lambda x: x[1], reverse = True) # 점수별 내림차수 정렬

    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")