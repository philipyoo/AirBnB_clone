#!/usr/bin/python3
from models import *

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__()
