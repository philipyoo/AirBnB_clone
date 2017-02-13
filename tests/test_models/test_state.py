import unittest
from datetime import datetime
from models import *


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.model = State()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
