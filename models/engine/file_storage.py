#!/usr/bin/python3
import json
import uuid


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj[0]] = obj[1]

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write("hello")

    def reload(self):
        with open(self.__file_path, mode="w+", encoding="utf-8") as fd:
            try:
                self.__objects = json.load(fd)
            except Exception:
                pass
