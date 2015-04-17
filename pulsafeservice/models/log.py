import datetime
from sqlalchemy import Column, Integer, Text, DateTime
from pulsafeservice.models import Base

class Log(Base):

    __tablename__ = 'logs'

    TYPE_LOG = {"heart_rate": "HEARTRATE"}

    id = Column(Integer, primary_key=True, nullable=False)
    user = Column(Text, nullable=False)
    datetime = Column(DateTime, nullable=False)
    type_log = Column(Text, nullable=False)
    value = Column(Text, nullable=False)

    def to_dict(self):
        result = super(Base, self).to_dict()
        result["datetime"] = self.datetime.strftime("%Y/%m/%d %H:%M:%S")
        return result
