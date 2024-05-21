#!/usr/bin/python3
"""
Tests for base_model.py --> BaseModel class
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """
        Testing the constructor
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Testing the save method
        """
        my_model = BaseModel()
        init_updated_at = my_model.updated_at
        curr_updated_at = my_model.save()
        self.assertNotEqual(init_updated_at, curr_updated_at)

    def test_to_dict(self):
        """
        Testing to_dict method
        """
        model = BaseModel()
        model_dict = model.to_dict
        message = "Object is not an instance of..."
        # self.assertIsInstance(model_dict, dict, message)
        self.assertEqual(model_dict()["__class__"], 'BaseModel')
        self.assertEqual(model_dict()['id'], model.id)
        self.assertEqual(model_dict()['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict()['updated_at'], model.updated_at.isoformat())

    def test_str_method(self):
        """
        Testing the str method
        """
        model = BaseModel()
        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))


if __name__ == "__main__":
    unittest.main()
