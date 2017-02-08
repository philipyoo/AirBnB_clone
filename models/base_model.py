#!/usr/bin/python3
import datetime, uuid
from models.engine.file_storage import FileStorage
storage=FileStorage()

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.created_at = str(datetime.datetime.now())
        self.id = str(uuid.uuid4())
        for i in args:
            if type(i) is dict:
                self.__dict__ = i
                storage.new(i)
        else:
            if kwargs is not None or kwargs != {}:
                for k, v in kwargs:
                    setattr(self, k, v)
                storage.new(self)

    def save(self):
        self.updated_at = str(datetime.datetime.now())
        storage.new(self)
        storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        dupe = self.__dict__.copy()
        dupe["__class__"] = type(self).__name__
        return dupe
