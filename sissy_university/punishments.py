from copy import deepcopy
from pprint import pprint

try:
    from .base_clases import Collection
    from .const import DATA_PUNISHMENTS
except ImportError:
    from base_clases import Collection
    from const import DATA_PUNISHMENTS



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
        self.parent = parent
        self.data = deepcopy(DEFAULT_PUNISHMENT)
        for k, v in kwargs.items():
            self.data[k] = v

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


class Punishments(Collection):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, datafile=DATA_PUNISHMENTS, base_class=Punishment)



if __name__ == "__main__":
    test = Punishments()
    print(test)
