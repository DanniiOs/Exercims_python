class Garden:
    PLANTS = {
        "V": "Violets",
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass"
    }
    CUPS_PER_STUDENT = 2

    def __init__(self, diagram,
                 students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                           "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
                           "Larry"]):
        self.students = sorted(students)
        self.diagram = diagram

    def plants(self, student):
        rows = self.diagram.split('\n')
        student_location = self.students.index(student)*self.CUPS_PER_STUDENT
        students_plants = []

        for row in rows:
            students_plants.append(self.PLANTS[row[student_location]])
            students_plants.append(self.PLANTS[row[student_location+1]])

        return students_plants
