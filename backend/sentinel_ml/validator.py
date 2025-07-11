from pydantic import BaseModel
from typing import List
# from datetime import date, time

# LineId,Date,Time,Pid,Level,Component,Content,EventId,EventTemplate
class InputRecord(BaseModel):
    LineId : int
    Date : str
    Time : str
    Pid : int
    Level : str
    Component : str
    Content : str
    EventId : str
    EventTemplate : str

class InputBatch(BaseModel):
    records : List[InputRecord]
