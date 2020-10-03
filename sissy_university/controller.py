"""
Controller interface between discord bot view and data model

**Author:**

   Ruffiana, ruffiana.plays@gmail.com, 9/28/2020
"""

try:
    from . import const
    from .collection import Collection
    from .data_io import Json
    from .major import Major
    from .course import Course
    from .club import Club
    from .partner import Partner
    from .punishment import Punishment
    from .roulette import Slot
except ImportError:
    import const
    from collection import Collection
    from data_io import Json
    from major import Major
    from course import Course
    from club import Club
    from partner import Partner
    from punishment import Punishment
    from roulette import Slot



class Controller(Json):
    def __init__(self, local=True):
        super().__init__()
        self._load(local=local)


    def __str__(self):
        return "\n".join([str(self.majors)])


    def _load(self, local=True):
        if local:
            self.majors = self._load_collection(Major, const.DATA_MAJORS)
            self.courses = self._load_collection(Course, const.DATA_COURSES)
            self.clubs = self._load_collection(Club, const.DATA_CLUBS)
            self.partners = self._load_collection(Partner, const.DATA_PARTNERS)
            self.punishments = self._load_collection(Punishment, const.DATA_PUNISHMENTS)
            self.roulette = self._load_collection(Slot, const.DATA_ROULETTE)


    def _load_json(self, base_class, filename):
        _dict = dict()
        _json = self.read_json(filename)
        for k, v in _json.items():
            # passing self in as 'collection' arguement so objects can access
            # the collection that they're a part of
            _dict[k] = base_class(self, **self.parse_dict(v))
        return _dict


    def _load_collection(self, base_class, filename, local=True):
        if local:
            _dict = self._load_json(base_class, filename)
            return Collection(self, _dict)



if __name__ == "__main__":
    test = Controller()
    print(test)

    print(test.majors)
    print(test.courses)
    print(test.clubs)
    print(test.partners)
    print(test.punishments)
    print(test.roulette)

    # test2 = test.majors.get_by_property("id", 11)
    # print(test2.prerequisites)