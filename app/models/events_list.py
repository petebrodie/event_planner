from app.models.event import *
from datetime import date


event1 = Event(date(2020, 5, 17), "Wedding", 6, "London", "Small Covid Wedding" )
event2 = Event(date(2021, 6, 25), "Birthday", 1, "Edinburgh", "Malcolm's lonely Birthday!")

events = [event1, event2]

def add_new_event(event):
    events.append(event)

