from copy import deepcopy
from pprint import pprint

try:
    from .base_clases import Collection
    from .const import DATA_ROULETTE
except ImportError:
    from base_clases import Collection
    from const import DATA_ROULETTE



DEFAULT_ROULETTE = {
    "imgUrl": "#",
    "title": "Teasing",
    "description": "Edge 2 times. You are not allowed to cum today!"
}



class Slot():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_ROULETTE)
        for k, v in kwargs.items():
            self.data[k] = v

    @property
    def title(self):
        return self.data.get("title")

    @property
    def name(self):
        return self.title

    @property
    def imgUrl(self):
        return self.data.get("imgUrl")

    @property
    def description(self):
        return self.data.get("description")



class Wheel(Collection):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, datafile=DATA_ROULETTE, base_class=Slot)

    def __str__(self):
        _str = [f"[{_id}] {obj.title} - {obj.description}" for _id, obj in self.collection.items()]
        return "\n".join(_str)


if __name__ == "__main__":
    test = Wheel()
    print(test)
