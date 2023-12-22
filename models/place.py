#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    place_amenity = Table('place_amenity',
                          Base.metadata, Column('place_id', String(60),
                                                ForeignKey('places.id'),
                                                primary_key=True,
                                                nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False), extend_existing=True)
    amenities = relationship('Amenity', secondary='place_amenity',
                             back_populates='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """Getter attribute in case of file storage"""
        from models import storage
        from models.reviews import Review
        reviews = []
        for k, v in storage.all(Review).items():
            if v.place_id == self.id:
                reviews.append(Review(**v))

        return reviews

    @property
    def amenities(self):
        """amenities"""
        amenity_ids_list = self.amenity_ids.split(',')
        return [Amenity.get(amenity_id) for amenity_id in amenity_ids_list if
                amenity_id]

    @amenities.setter
    def amenities(self, amenity_obj):
        """Setter attribute that appends Amenity.id to amenity_ids."""
        if isinstance(amenity_obj, Amenity):
            amenity_id = amenity_obj.id
            if self.amenity_ids:
                self.amenity_ids.append(amenity_id)
            else:
                self.amenity_ids = [amenity_id]
            self.save()
