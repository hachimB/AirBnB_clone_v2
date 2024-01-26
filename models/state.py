#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', cascade='all, delete-orphan', backref='state')

    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(City(**city))
        return city_list
