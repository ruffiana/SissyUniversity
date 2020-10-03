from copy import deepcopy
from pprint import pprint



DEFAULT_CLUB = {
    "days": "0",
    "description": "Time to show off your sexy body.",
    "id": "1",
    "imgUrl": "1381",
    "job1": "Wear nothing but panties and a bra while performing your task(s).",
    "job2": "In addition to Option 1 wear stockings and heels while performing your task(s).",
    "name": "Stripping club",
    "perk1": "Reduce all task requirements by 8%",
    "perk2": "Reduce all task requirements by 8%",
    "tier": "1",
    "type": "club"
    }



class Club():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_CLUB)
        for k, v in kwargs.items():
            self.data[k] = v


    def __str__(self):
        return f"[{self.id}] {self.name} - {self.description}"


    def as_list(self):
        return f"{self.id} - {self.name}"


    @property
    def name(self):
        return self.data.get("name")


    @property
    def days(self):
        return self.data.get("days")


    @property
    def description(self):
        return self.data.get("description")


    @property
    def id(self):
        return self.data.get("id")


    @property
    def imgUrl(self):
        return self.data.get("imgUrl")


    @property
    def job1(self):
        return self.data.get("job1")


    @property
    def job2(self):
        return self.data.get("job2")


    @property
    def perk1(self):
        return self.data.get("perk1")


    @property
    def perk2(self):
        return self.data.get("perk2")


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
    test = Clubs()
    print(test)
