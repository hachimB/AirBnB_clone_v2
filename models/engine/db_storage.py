#!/usr/bin/python3
"""Module documentation"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from os import environ
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class for managing database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """init method"""

        Session = sessionmaker(bind=self.__engine)
        self.__engine = Session()

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            environ.get('HBNB_MYSQL_USER'),
            environ.get('HBNB_MYSQL_PWD'),
            environ.get('HBNB_MYSQL_HOST'),
            environ.get('HBNB_MYSQL_DB')
        ), pool_pre_ping=True)

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all """
        if cls:
            objects = self.__session.query(cls).all()

            _dict_ = {}

            for obj in objects:
                _dict_['{}.{}'.format(
                    obj.__class__.__name__, obj.id
                )] = obj

            return _dict_

        objects = self.__session.query(
            User, State, City, Amenity, Place, Review
        ).all()

        for obj in objects:
            _dict_['{}.{}'.format(
                obj.__class__.__name__, obj.id
            )] = obj

    def new(self, obj):
        """new obj in the database"""
        self.__session.add(obj)

    def save(self, obj):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
