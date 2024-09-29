import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from forms import NameForm

class TestNameForm(unittest.TestCase):
    def test_form_valid(self):
        form = NameForm(first_name="John", last_name="Doe")
        self.assertTrue(form.validate())

    def test_form_invalid_missing_first_name(self):
        form = NameForm(first_name="", last_name="Doe")
        self.assertFalse(form.validate())

    def test_form_invalid_missing_last_name(self):
        form = NameForm(first_name="John", last_name="")
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()
