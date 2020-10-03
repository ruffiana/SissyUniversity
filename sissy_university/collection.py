# from fuzzywuzzy import fuzz



class Collection():
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

    def __init__(self, parent, collection):
        super().__init__()
        self.parent = parent
        self.collection = collection


    def __str__(self):
        return "\n".join(self.as_list())


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


    def as_list(self):
        _sorted = [
            self.collection[key].as_list()
            for key in sorted(self.collection.keys(), key=int)
            ]
                    
        return _sorted
