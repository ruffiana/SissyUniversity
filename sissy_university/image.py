from copy import deepcopy
from pprint import pprint

try:
    from .base_clases import Collection
    from .const import DATA_IMAGES
except ImportError:
    from base_clases import Collection
    from const import DATA_IMAGES



DEFAULT_IMAGE = {
    "id": "1",
    "url": "img/image1",
    "author": "",
    "authorUrl": "",
    "tags": "",
    "toys": "",
    "clothes": ""
    }


class Image():
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.parent = parent
        self.data = deepcopy(DEFAULT_IMAGE)
        for k, v in kwargs.items():
            self.data[k] = v

    @property
    def id(self):
        return self.data.get("id")

    @property
    def url(self):
        return self.data.get("url")

    @property
    def author(self):
        return self.data.get("author")

    @property
    def authorUrl(self):
        return self.data.get("authorUrl")

    @property
    def tags(self):
        return self.data.get("tags")

    @property
    def toys(self):
        return self.data.get("toys")

    @property
    def clothes(self):
        return self.data.get("clothes")



class Gallery(Collection):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, datafile=DATA_IMAGES, base_class=Image)


    def __str__(self):
        _str = [f"[{_id}] - {obj.url}" for _id, obj in self.collection.items()]
        return "\n".join(_str)



if __name__ == "__main__":
    test = Gallery()
    print(test)
