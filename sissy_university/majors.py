from copy import deepcopy
from pprint import pprint
import uuid

try:
    from .base_clases import Collection
    from .const import DATA_MAJORS
except ImportError:
    from base_clases import Collection
    from const import DATA_MAJORS


DEFAULT_MAJOR = {
    "id": "13",
    "imgUrl": "#",
    "type": "major",
    "name": "Sex Slavery",
    "name2": "bondage, masochism, submission",
    "prerequisites": "414 420",
    "description": "You will become a sex slave who derives pleasure from pain.",
    "tier": "major",
    "daily1": "none",
    "daily2": "none",
    "exam1": "Gag yourself. Make a clothespin zipper that runs from one of your breasts, around your navel and back to the other breast (20 clothespins minimum). Keep it on and spank your ass until it becomes red (50 times minimum). Then pull the zipper hard and fast.",
    "exam2": "Attach clothespins to your nipples and insert a buttplug/vibrator/dildo in your ass. Tie yourself in a hogtie/frog-tie/mummy-tie for 60minutes while blindfolded and gagged.",
    "exam3": "Go in chat or online and request 10 slave tasks to perform which preferably include bondage and pain. Spank your ass hard 20 times and your balls/pussy 10 times for every task you refuse.",
    "tags": "slave"
    }


class Major():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_MAJOR)
        for k, v in kwargs.items():
            self.data[k] = v

    def __str__(self):
        return f"[{self.id}] {self.name} - {self.description}"

    @property
    def id(self):
        return self.data.get("id")

    @property
    def imgUrl(self):
        return self.data.get("imgUrl")

    @property
    def type(self):
        return self.data.get("type")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def name2(self):
        return self.data.get("name2")

    @property
    def prerequisites(self):
        prerequisites = self.data.get("prerequisites")
        if isinstance(prerequisites, int):
            prerequisites = [prerequisites]
        else:
            prerequisites = [int(i) for i in prerequisites.split()]
        # prerequisites for majors are courses
        return [self.parent.parent.courses.get_by_property("id", _id) for _id in prerequisites]
        # return self.data.get("prerequisites")

    @property
    def description(self):
        return self.data.get("description")

    @property
    def tier(self):
        return self.data.get("tier")

    @property
    def locked(self):
        return self.tier > 1

    @property
    def daily1(self):
        return self.data.get("daily1")

    @property
    def daily2(self):
        return self.data.get("daily2")

    @property
    def exam1(self):
        return self.data.get("exam1")

    @property
    def exam2(self):
        return self.data.get("exam2")

    @property
    def exam3(self):
        return self.data.get("exam3")

    @property
    def tags(self):
        return self.data.get("tags")



class Majors(Collection):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, datafile=DATA_MAJORS, base_class=Major)


if __name__ == "__main__":
    test = Majors()
    print(test)

    test2 = test.get_by_property('id', 1)
    print(test2.prerequisites)
