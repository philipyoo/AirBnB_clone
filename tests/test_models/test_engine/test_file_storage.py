import unittest
import os.path
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import *


class Test_FileStorage(unittest.TestCase):
    """
    Test the file storage class
    """

    def setUp(self):
        self.store = FileStorage()

        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

    def tearDown(self):
        import os
        os.remove('file.json')

    def test_all(self):
        test_len = 0
        if os.path.isfile("file.json"):
            test_len = len(self.store.all())

        self.assertEqual(len(self.store.all()), test_len)

    def test_new(self):
        pass

    def test_save(self):
        test_len = 0
        if os.path.isfile("file.json"):
            test_len = len(self.store.all())

        self.assertEqual(len(self.store.all()), test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), test_len + 1)

    def test_reload(self):
        pass


if __name__ == "__main__":
    unittest.main()
