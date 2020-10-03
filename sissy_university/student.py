from copy import deepcopy
from datetime import datetime, timedelta
import time
import uuid

try:
    from .const import *
    from .data_io import SuSave
except ImportError:
    from const import *
    from data_io import SuSave
    


DEFAULT_STUDENT = {
    "id": None,
    "name": "Jane Doe",
    "IsSubmittedProgressToday": False,
    "activeClubs": [],
    "activePartnerPerks": [],
    "activePartners": [],
    "activePerks": [],
    "activePerksNum": 0,
    "attendedClasses": [],
    "attendedClassesToday": [],
    "classSkipsAvailable": 0,
    "clubActivitiesDoneNum": 0,
    "clubTaskMultiplier": 0,
    "communityContentStatus": True,
    "completedClasses": [],
    "completedMajors": [],
    "currentClasses": [],
    "currentCredits": 0,
    "currentMajor": 0,
    "currentPunishments": [],
    "difficulty": 1,
    "difficultyTaskMultiplier": 0,
    "easyMode": False,
    "finalTaskMultiplier": 1,
    "finalThesisInProgress": False,
    "firstRun": False,
    "gameVersion": 2.2,
    "hardcorePunishmentsStatus": False,
    "lastDate": 27,
    "maxActiveClubs": 5,
    "maxActivePerks": 10,
    "punishmentsDoneNum": 0,
    "requiredCredits": 160,
    "tasks": [],
    "todayClasses": [],
    "view": "settings"
}



class Student(SuSave):
    def __init__(self, filename=None, **kwargs):
        super().__init__()
        if filename:
            self.data = self.load(filename)
        else:
            self.data = deepcopy(DEFAULT_STUDENT)

        for k, v in kwargs:
            self.data[k] = v

        if not self.id:
            self.id = self._new_id()

    
    def __str__(self):
        return f"{self.name} - {self.id}"

    def __repr__(self):
        return self.data

    @staticmethod
    def _new_id():
        """
        [description]
        
        **Arguments:**
        
            None
        
        **Keyword Arguments:**
        
            None

        **Notes:**
        
            Student ID format is SU[enrollment_year][enrollment_month][####]

        **Returns:**
        
            :``str``: Unique student id as a string
        
        **Author:**
        
            ruffiana, ruffiana.plays@gmail.com, 9/27/2020
        """

        # id format is SU[year][semester][birthday_month][birthday_day][####]
        cur_date_time = datetime.fromtimestamp(time.time())
        year, month = (cur_date_time.year, cur_date_time.month)
        return f"SU{year}{month}0001"

    @property
    def name(self):
        return self.data.get("name")

    @property
    def id(self):
        return self.data.get("id")

    @id.setter
    def id(self, id):
        self.data['id'] = id

    @property
    def IsSubmittedProgressToday(self):
        return self.data.get("IsSubmittedProgressToday")

    @property
    def activeClubs(self):
        return self.data.get("activeClubs")

    @property
    def activePartnerPerks(self):
        return self.data.get("activePartnerPerks")

    @property
    def activePartners(self):
        return self.data.get("activePartners")

    @property
    def activePerks(self):
        return self.data.get("activePerks")

    @property
    def activePerksNum(self):
        return len(self.data.get("activePerks"))

    @property
    def attendedClasses(self):
        return self.data.get("attendedClasses")

    @property
    def attendedClassesToday(self):
        return self.data.get("attendedClassesToday")

    @property
    def classSkipsAvailable(self):
        return self.data.get("classSkipsAvailable")

    @property
    def clubActivitiesDoneNum(self):
        return self.data.get("clubActivitiesDoneNum")

    @property
    def clubTaskMultiplier(self):
        return self.data.get("clubTaskMultiplier")

    @property
    def communityContentStatus(self):
        return self.data.get("communityContentStatus")

    @property
    def completedClasses(self):
        return self.data.get("completedClasses")

    @property
    def completedMajors(self):
        return self.data.get("completedMajors")

    @property
    def currentClasses(self):
        return self.data.get("currentClasses")

    @property
    def currentCredits(self):
        return self.data.get("currentCredits")

    @property
    def currentMajor(self):
        return self.data.get("currentMajor")

    @property
    def currentPunishments(self):
        return self.data.get("currentPunishments")

    @property
    def difficulty(self):
        return self.data.get("difficulty")

    @property
    def difficultyTaskMultiplier(self):
        return self.data.get("difficultyTaskMultiplier")

    @property
    def easyMode(self):
        return self.data.get("easyMode")

    @property
    def finalTaskMultiplier(self):
        return self.data.get("finalTaskMultiplier")

    @property
    def finalThesisInProgress(self):
        return self.data.get("finalThesisInProgress")

    @property
    def firstRun(self):
        return self.data.get("firstRun")

    @property
    def gameVersion(self):
        return self.data.get("gameVersion")

    @property
    def hardcorePunishmentsStatus(self):
        return self.data.get("hardcorePunishmentsStatus")

    @property
    def lastDate(self):
        return self.data.get("lastDate")

    @property
    def maxActiveClubs(self):
        return self.data.get("maxActiveClubs")

    @property
    def maxActivePerks(self):
        return self.data.get("maxActivePerks")

    @property
    def punishmentsDoneNum(self):
        return self.data.get("punishmentsDoneNum")

    @property
    def requiredCredits(self):
        return self.data.get("requiredCredits")

    @property
    def tasks(self):
        return self.data.get("tasks")

    @property
    def todayClasses(self):
        return self.data.get("todayClasses")

    @property
    def view(self):
        return self.data.get("view")



if __name__ == "__main__":
    # filename = PATH_DATA / "save2020-09-25.suSave"
    # test = Student(filename)
    # print(test)

    test2 = Student()
    print(test2)

    from pprint import pprint
    pprint(test2.__repr__())    
    # db = Postgress()