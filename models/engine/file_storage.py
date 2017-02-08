#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            self.__objects[obj.id] = obj.__dict__

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(self.__objects))

    def reload(self):
        with open(self.__file_path, mode="w+", encoding="utf-8") as fd:
            try:
                self.__objects = json.load(fd)
            except Exception:
                pass
