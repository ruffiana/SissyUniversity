try:
    from .majors import Majors
    from .courses import Courses
    from .clubs import Clubs
    from .partners import Partners
    from .punishments import Punishments
    from .roulette import Wheel
except ImportError:
    from majors import Majors
    from courses import Courses
    from clubs import Clubs
    from partners import Partners
    from punishments import Punishments
    from roulette import Wheel



class Data():
    def __init__(self, local=True):
        super().__init__()
        self._load(local=local)

    def _load(self, local=True):
        self.majors = Majors(parent=self)
        self.courses = Courses(parent=self)
        self.clubs = Clubs(parent=self)
        self.partners = Partners(parent=self)
        self.punishments = Punishments(parent=self)
        self.roulette = Wheel(parent=self)

    def __str__(self):
        return "\n".join([str(self.majors)])


if __name__ == "__main__":
    test = Data()
    print(test)

    test2 = test.majors.get_by_property("id", 11)
    print(test2.prerequisites)