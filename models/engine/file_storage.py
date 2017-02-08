#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj.__dict__

    def save(self):
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(FileStorage.__objects))

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r+", encoding="utf-8") as fd:
                try:
                    FileStorage.__objects = json.load(fd)
                except Exception as e:
                    print("Error storing json:", e)
        except Exception:
            pass
