"""
Reading/Writing data from local files or online databases

**Author:**

    Ruffiana, ruffiana.plays@gmail.com, 9/28/2020
"""

import ast
import os
import sys
import json
import urllib
from pprint import pprint
import pickle
from pathlib import Path

from dotenv import load_dotenv
import redis
import psycopg2

try:
    from .const import PATH_DATA
except ImportError:
    from const import PATH_DATA



class Json():
    def __init__(self):
        super().__init__()


    @classmethod
    def read_json(cls, filename, first=True, byteify=False):
        if not Path(filename).exists():
            print(f"{filename} does not exist!")
            return None
        try:
            with open(filename) as f:
                if byteify:
                   _dict = json.load(f, object_hook=cls._byteify)
                else:
                    _dict = json.load(f)
        except Exception as e:
            print(f"Failed reading {filename}!!\n{e}")
            return None
        
        if first and isinstance(_dict, list):
            _dict = _dict[0]
        
        return _dict


    @staticmethod
    def write_json(data, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, sort_keys=True, indent=4)
            return True
        except Exception as e:
            print(f"Failed writing {filename}!\n{e}")
            return False


    @classmethod
    def _parse_value(cls, val):
        constants  = {
            "false" : False,
            "true" : True,
            "null" : None,
            "none" : None
        }

        if val in constants.keys():
            return constants.get(val)

        try:
            return ast.literal_eval(val)
        except:
            return val


    @classmethod
    def parse_dict(cls, _dict):
        _dict = {k : cls._parse_value(v) for k, v in _dict.items()}
        return _dict


    @classmethod
    def _byteify(cls, data, ignore_dicts=False):
        if isinstance(data, str):
            return data

        # if this is a list of values, return list of byteified values
        if isinstance(data, list):
            return [cls._byteify(item, ignore_dicts=True) for item in data]

        # if this is a dictionary, return dictionary of byteified keys and values
        # but only if we haven"t already byteified it
        if isinstance(data, dict) and not ignore_dicts:
            return {
                    cls._byteify(key, ignore_dicts=True): cls._byteify(value, ignore_dicts=True)
                    for key, value in data.items()
            }
        return data


class SuSave(Json):
    def __init__(self, filename=None):
        super().__init__()
        if filename:
            self.data = self.load(filename)


    def __str__(self):
        return json.dumps(self.data, sort_keys=True, indent=4)


    def __repr__(self):
        return self.data


    def load(self, filename):
        """
        Load and parse a .suSave file into Python dict
        
        **Arguments:**
        
            :``filename``: `str` Filepath to .suSave file
        
        **Keyword Arguments:**
        
            None
        
        **Returns:**
        
            :``dict``: Save file data as dict
        
        **Author:**
        
            ruffiana, ruffiana.plays@gmail.com, 9/25/2020
        """
        _json = self.read_json(filename, byteify=True)
        _json = self._byteify(_json, ignore_dicts=True)
        if not _json:
            return None
        _dict = {k : self._parse_value(v) for k, v in _json.items()}
        return _dict


class Redis(Json):
    def __init__(self):
        super().__init__()
        self.db = self._init_db()


    def _init_db(self):
        if not 'REDISCLOUD_URL' in os.environ:
            load_dotenv()
        url = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL'))
        try:
            return redis.Redis(
                host=url_redis.hostname,
                port=url_redis.port,
                password=url_redis.password)
        except:
            print('Unable to connect to Redis database.')
            return None


    def upload(self, filename, key): 
        _dict = self.read_json(filename)
        # serialize dict as string and write to redis DB
        conn.set(key, pickle.dumps(_dict))
        return True


    def download(self, filename, key):
        _dict = pickle.loads(conn.get(key))
        self.write_json(_dict, filename)
        pprint(_dict)
        return True


class Postgress(Json):
    """
    [description]
    
    **Arguments:**
    
        None
    
    **Keyword Arguments:**
    
        None

    **Notes:**
    
        https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
        https://kb.objectrocket.com/postgresql/insert-json-data-into-postgresql-using-python-part-2-1248

    **Author:**
    
        Ruffiana, ruffiana.plays@gmail.com, 9/26/2020
    """

    def __init__(self):
        super().__init__()
        self._init_db()


    def _init_db(self):
        """
        [description]
        
        **Arguments:**
        
            None
        
        **Keyword Arguments:**
        
            None

        **Notes:**

            postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
        
        **Returns:**
        
            :``[type]``: [description]
        
        **Author:**
        
            Ruffiana, ruffiana.plays@gmail.com, 9/26/2020
        """

        if not 'POSTGRESS_URL' in os.environ:
            load_dotenv()
        self.url = os.environ.get('POSTGRESS_URL')

        try:
            self.db = psycopg2.connect(self.url)
            self.cursor = self.db.cursor()
        except:
            print(f'Unable to connect to Postgress database!')


    def upload(self, filename, key): 
        _dict = self.read_json(filename)
        # https://kb.objectrocket.com/postgresql/insert-json-data-into-postgresql-using-python-part-2-1248
        return True


    def dowload(self, filename, key):
        # build dict from postgress DB
        self.write_json(_dict, filename)
        pprint(_dict)
        return True



if __name__ == "__main__":
    filename = PATH_DATA / "save2020-09-25.suSave"
    test = SuSave(filename)
    print(test)

    # db = Postgress()