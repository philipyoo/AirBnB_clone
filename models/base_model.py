#!/usr/bin/python3
import datetime, uuid
from models.engine import FileStorage
storage=FileStorage()

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.created_at = str(datetime.datetime.now())
        self.id = str(uuid.uuid4())
        for i in args:
            if type(i) is dict:
                self.__dict__ = i
                break
        else:
            if kwargs is not None:
                new_obj = {}
                for k, v in kwargs:
                    new_obj = {k, v}
                    storage.new(new_obj)

    def save(self):
        print("entering save")
        self.updated_at = str(datetime.datetime.now())
        storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        dupe = self.__dict__.copy()
        dupe["__class__"] = type(self).__name__
        return dupe
