from copy import deepcopy
from pprint import pprint



DEFAULT_PARTNER = {
    "description": "Zoe is a second year Domination Studies major at the university and as such she needs to pick a play-partner for her penetration classes. Luckily she has noticed you and would love to have you as her sex toy for the rest of the year.",
    "id": "1",
    "imgUrl": "1382",
    "job1": "Increase the requirements for all Penetration tasks by 25%",
    "job2": "Increase the requirements for all Penetration tasks by 25%",
    "name": "Zoe",
    "name2": "anal oral",
    "perk1": "Penetration tasks will give you an additional 1 point.",
    "perk2": "Penetration tasks will give you an additional 1 point.",
    "tags": "penetration",
    "tier": "1",
    "type": "partner"
    }



class Partner():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_PARTNER)
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
    def name(self):
        return self.data.get("name")


    @property
    def name2(self):
        return self.data.get("name2")


    @property
    def perk1(self):
        return self.data.get("perk1")


    @property
    def perk2(self):
        return self.data.get("perk2")


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
    test = Partners()
    print(test)
