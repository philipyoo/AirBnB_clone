#!/usr/bin/python3
import json


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, mode="w+", encoding="utf-8") as fd:
            fd.write(json.dumps(self.all()))

    def reload(self):
        with open(self.__file_path, mode="w+", encoding="utf-8") as fd:
            self.__objects = json.loads(fd)
