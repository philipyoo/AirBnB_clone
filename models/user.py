#!/usr/bin/python3
from models import *


def User(BaseModel):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(self, *args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
