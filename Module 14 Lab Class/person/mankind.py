""" All about mankind """
class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, cases, nationality, gender, height, weight):
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CsEngineer(Human):
    def __init__(self, Love_to_code, has_gf,gender, height, weight):
        super().__init__(gender, height, weight)
        self.Love_to_code = Love_to_code
        self.has_gf = has_gf

if __name__ == '__main__':

    police = Police(True, "Bangladeshi", "Male", 55, 78)
    print(police.height)

    eng = CsEngineer(True, False, 'make', 78,65)
    print(eng.weight)

    eng2 = CsEngineer(height=70, weight= 45, has_gf=False, Love_to_code=True,gender='Male')
    print(eng2.height)