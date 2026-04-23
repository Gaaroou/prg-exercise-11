
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body > 90 and body < 101:
            return "A"
        elif body in range(80,90):
            return  "B"
        elif body in range(70,80):
            return  "C"
        elif body in range(60,70):
            return  "D"
        elif body in range(50,60):
            return  "E"
        elif body in range(0,50):
            return  "F"

    def find(self, hledane_cislo):
        idx = []
        score = self.scores
        for i in range(len(score)-1):
            if score[i] == hledane_cislo:
                idx.append(i)
        return idx

    def get_sorted(self):
        seznam = self.scores.copy()

        for x in range(len(seznam)):
            for y in range(len(seznam) - 1):
                if seznam[y] > seznam[y + 1]:
                    seznam[y], seznam[y + 1] = seznam[y + 1], seznam[y]
        return seznam

def main():
    results1 = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet = results1.count()

    print(pocet)
    for i in range(pocet):
        body = results1.get_by_index(i)
        znamka = results1.get_grade(i)
        print(f"Student {i}: {body} points – {znamka}")

    for i in range(pocet):
        body = results1.get_by_index(i)
        if body == 100:
            print(i)

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    main()

