class ExamSubmission:
    def __init__(self, examinee:str, points:int):
        self.examinee:str = examinee
        self.points:int = points

def passed(submissions:list[ExamSubmission], lowest_passing:int) -> list[ExamSubmission]:
    return [submission for submission in submissions if submission.points >= lowest_passing]

def main():
    iivari = ExamSubmission('Iivari', 100)
    joulupukki = ExamSubmission('Joulupukki', 57)
    joulumuori = ExamSubmission('Joulumuori', 61)

    passed_examinees = passed([iivari, joulupukki, joulumuori], 60)
    for examinee in passed_examinees:
        print(f"This person passed: {examinee.examinee}")


if __name__ == '__main__':
    main()