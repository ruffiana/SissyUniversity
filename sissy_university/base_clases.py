from fuzzywuzzy import fuzz

try:
    from .data_io import Json
except ImportError:
    from data_io import Json



class Collection(Json):
    """
    Base class for collection of data objects
    
    **Arguments:**
    
        :``datafile``: `str` Filename for local datafile
        :``base_class``: `class` Class to instantiate for entires in this collection
    
    **Keyword Arguments:**
    
        :``local``: `bool` If true, load data from local source. Default is True.
    
    **Author:**
    
        Ruffiana, ruffiana.plays@gmail.com, 9/28/2020
    """

    def __init__(self, datafile, base_class, parent=None, local=True):
        super().__init__()
        self.parent = parent
        self.datafile = datafile
        self.base_class = base_class
        self.collection = self._load(local=local)

    def __str__(self):
        _str = [f"[{_id}] - {obj.name}" for _id, obj in self.collection.items()]
        return "\n".join(_str)

    def _load(self, local=True):
        if local:
            return self._load_from_local()
        else:
            # load from DB commands
            pass

    def _load_from_local(self):
        _dict = dict()
        _json = self.read_json(self.datafile)
        for k, v in _json.items():
            # passing self in as 'collection' arguement so objects can access
            # the collection that they're a part of
            _dict[k] = self.base_class(self, **self.parse_dict(v))
        return _dict

    def get_by_property(self, _property, value):
        if isinstance(value, str):
            value = value.lower()

        for k, obj in self.collection.items():
            if not hasattr(obj, _property):
                continue
            val2 = getattr(obj, _property)
            if isinstance(val2, str):
                val2 = val2.lower()
            # try to find case-insensitive match first
            if value == val2:
                return obj
            # # look for fuzzy match    
            # if fuzz.ratio(value, val2) > 75:
            #     return obj
        return None
