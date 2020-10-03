from copy import deepcopy
from pprint import pprint



DEFAULT_PUNISHMENT = {
    "description": "You are forced to write a degrading term on your body and keep it on for the rest of your workload ( Minimum 60minutes ). \"Example\": slut, whore, slave, fucktoy etc",
    "id": "10",
    "imgUrl": "101",
    "name": "Humiliation",
    "tier": "1",
    "type": "punishment"
}



class Punishment():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.data = deepcopy(DEFAULT_PUNISHMENT)
        for k, v in kwargs.items():
            self.data[k] = v


    def __str__(self):
        return f"[{self.id}] {self.name} - {self.description}"


    def as_list(self):
        return f"{self.id} - {self.name}"


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
    def name(self):
        return self.data.get("name")


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
    test = Punishments()
    print(test)
