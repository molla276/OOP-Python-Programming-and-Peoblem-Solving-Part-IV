class School:
    def __init__(self, name):
        self.school_name = name
        print('School init called')

class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print('Grade Class init called')

class Sports:
    def __init__(self, sports_name):
        self.sports_name = sports_name
        self.team = []

    def add_player(self, player_name):
        self.team.append(player_name)

class Student(School, Grade, Sports):
    def __init__(self, name, grade_name, school_name,sports_name):
        self.name = name
        print('Student class init called')
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)
        Sports.__init__(self, sports_name)

ananta_j = Student('Aj', 'MBA', 'UK School', 'Football')
print(ananta_j.name)
print(ananta_j.grade_name)
print(ananta_j.school_name)
print(ananta_j.sports_name)
ananta_j.add_player('Borsha')
ananta_j.add_player('AJ')
print(ananta_j.team)