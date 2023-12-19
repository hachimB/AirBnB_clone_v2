#!/usr/bin/python3
"""Module documentation"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from os import environ

from state import State


class DBStorage():
    """Class for managing database storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            environ.get('HBNB_MYSQL_USER'),
            environ.get('HBNB_MYSQL_PWD'),
            environ.get('HBNB_MYSQL_HOST'),
            environ.get('HBNB_MYSQL_DB')
        ), pool_pre_ping=True)

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            objects = self.__session.query(cls).all()

            _dict_ = {}

            for obj in objects:
                _dict_['{}.{}'.format(
                    obj.__class__, obj.id
                )] = obj

            return _dict_

        objects = self.__session.query(
            User, State, City, Amenity, Place, Review
        ).all()

        for obj in objects:
            _dict_['{}.{}'.format(
                obj.__class__, obj.id
            )] = obj
