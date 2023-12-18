#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import console
from models import storage
import os


class test_Console(unittest.TestCase):
    """ Class to test the file console"""

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]
    
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass
    
    def test_create(self):
        """ Test create command """
        console.do_create("BaseModel")
        console.do_create("User")
        console.do_create("State")
        console.do_create("City")
        console.do_create("Amenity")
        console.do_create("Place")
        console.do_create("Review")
        self.assertEqual(len(storage.all()), 7)
    
    def test_show(self):
        """ Test show command """
        console.do_create("BaseModel")
        console.do_show("BaseModel " + console.b_id)
        self.assertEqual(console.b_id, console.b_id)
        