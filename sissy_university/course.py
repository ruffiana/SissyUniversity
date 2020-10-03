import calendar
from copy import deepcopy
from pprint import pprint



DEFAULT_COURSE = {
    "community": False,
    "daily1": "Spend 30minutes in underwear only.",
    "daily2": "Spend 15minutes completely naked.",
    "days": "1 5",
    "description": "You will get comfortable with the idea of showing your skin. (This is a beginner class)",
    "exam1": "Spend 60minutes in underwear.",
    "exam2": "Spend 30minutes completely naked.",
    "id": "1001",
    "imgUrl": "1316",
    "name": "Undressing",
    "name2": "nudity",
    "prerequisites": "",
    "tags": "nudity",
    "tier": "beginner",
    "type": "class"
    }



class Course():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_COURSE)
        for k, v in kwargs.items():
            self.data[k] = v


    def __str__(self):
        return f"[{self.id}] {self.name} - {self.description}"


    def as_list(self):
        return f"{self.id} - {self.name}"


    @property
    def id(self):
        return self.data.get("id")


    @property
    def name(self):
        return self.data.get("name")


    @property
    def name2(self):
        return self.data.get("name2")


    @property
    def description(self):
        return self.data.get("description")


    @property
    def community(self):
        return self.data.get("community")


    @property
    def days(self):
        days = self.data.get("days")
        if not days:
            return None
        days = days.split()
        return [calendar.day_name[int(i)] for i in days]


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
    def imgUrl(self):
        return self.data.get("imgUrl")


    @property
    def prerequisites(self):
        prerequisites = self.data.get("prerequisites")
        if isinstance(prerequisites, int):
            prerequisites = [prerequisites]
        else:
            prerequisites = [int(i) for i in prerequisites.split()]
        return [self.parent.get_by_property("id", _id) for _id in prerequisites]
        # return self.data.get("prerequisites")


    @property
    def tags(self):
        return self.data.get("tags")


    @property
    def tier(self):
        return self.data.get("tier")


    @property
    def locked(self):
        return self.tier > 1


    @property
    def type(self):
        return self.data.get("type")



if __name__ == "__main__":
    test = Courses()
    print(test)
