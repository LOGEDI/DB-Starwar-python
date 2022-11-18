import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planet_id = Column(Integer,ForeignKey('planet.id'))
    character_id = Column(Integer,ForeignKey('people.id'))
    #person = relationship(Person)

    

class Favoriteplanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer,ForeignKey('user.id'))
   # person = relationship(Person)

      

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
   # person = relationship(Person)

    

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_Character'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer,ForeignKey('user.id'))
    character_id = Column(Integer,ForeignKey('character.id'))
   # person = relationship(Person)
         
   

#class Favorite(Base):
   # __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
   # user_id = Column(Integer,ForeignKey('user.id'))
    #planet_id = Column(Integer, ForeignKey('planet.id'))
   # person_id = Column(Integer, ForeignKey('person.id'))
    #fav_id = Column (Integer,ForeignKey('fav.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
