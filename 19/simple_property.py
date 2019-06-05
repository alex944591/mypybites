from datetime import datetime
from datetime import timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, str, datetime):
        self.str=str
        self.datetime=datetime
         # getting the values
    def getValue(self):
        delta=NOW-self.datetime
        if delta.seconds>0:
            return True
        else:
            return False
    expired = property(getValue)
