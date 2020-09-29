"""
Collection of tools and functions for managing/updating local data files

**Author:**

    Ruffiana, ruffiana.plays@gmail.com, 9/28/2020
"""

import json
from pprint import pprint

try:
    from .data import Json
    from .const import *
except ImportError:
    from data import Json
    from const import *



def upate_imageUrl_values():
    """
    Update .json data files with mapped id of images
    
    **Arguments:**
    
        None
    
    **Keyword Arguments:**
    
        None
    
    **Author:**
    
        Ruffiana, ruffiana.plays@gmail.com, 9/27/2020
    """

    image_map = Json.read_json(PATH_DATA / "image_map.json")

    map_key_datafile = {
        'MajorsImages' : DATA_MAJORS,
        'ClassesImages' : DATA_CLASSES,
        'PartnersImages' : DATA_PARTNERS,
        'ClubsImages' : DATA_CLUBS,
        'PunishmentsImages' : DATA_PUNISHMENTS,
    }

    for key_name, datafile in map_key_datafile.items():
        _dict = Json.read_json(datafile)
        image_ids = image_map.get(key_name)
        for _id, values in _dict.items():
            image_id = image_ids.get(_id)           
            _dict[_id]["imgUrl"] = str(image_id)
        pprint(_dict)

        Json.write_json(_dict, datafile)



if __name__ == "__main__":
    pass
    # upate_imageUrl_values()