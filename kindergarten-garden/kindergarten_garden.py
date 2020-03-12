class Garden:
    students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    plant = {'G': "Grass", 'C': "Clover", 'V': "Violets", 'R': "Radishes"}

    def __init__(self, diagram, students = students):
        self.students = students
        self.students.sort()
        self.diagram = diagram

    def plants(self, name):
        index = self.students.index(name)
        st_index = index * 2
        p = []
        for e in self.diagram.split():
            p.append(self.plant.get(e[st_index]))
            p.append(self.plant.get(e[st_index + 1]))
        return p
