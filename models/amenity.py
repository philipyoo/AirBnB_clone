#!/usr/bin/python3
from models import *


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__()
