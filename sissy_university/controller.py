"""
Controller interface between discord bot view and data model

**Author:**

   Ruffiana, ruffiana.plays@gmail.com, 9/28/2020
"""

try:
    from .model import Data
except ImportError:
    from model import Data

data = Data()



if __name__ == "__main__":
    print(data)
