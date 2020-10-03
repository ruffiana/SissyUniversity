from copy import deepcopy
from pprint import pprint



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


    def __str__(self):
        return f"{self.name} - {self.description}"


    def as_list(self):
        return f"{self.name} - {self.description}"


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



if __name__ == "__main__":
    test = Wheel()
    print(test)

    