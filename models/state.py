#!/usr/bin/python3
from models import *

class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
        self.name = ""
