class Schedule():
    def __init__(self, **kwargs):
        super().__init__()
        self.data = {
            "name": None,
        }
        for k, v in kwargs:
            self.data[k] = v

    @property
    def name():
        return self.data.get("name")
