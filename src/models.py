import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(120), nullable=True)
    password = Column(String(80), nullable=True)
    is_active = Column(Boolean(), nullable=False)



class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False) 
    skin_color = Column(String(250), nullable=False) 
    species = Column(String(250), nullable=False) 
    gender = Column(String(250), nullable=False)

class Characters_Fav(Base):
    __tablename__ = "characters_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    user_to = relationship("users",foreign_keys=[user_id])
    character_id = Column(Integer, ForeignKey("characters.id")) 
    character_fav = relationship("characters",foreign_keys=[character_id])

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Float, nullable=False) 
    diameter = Column(Float, nullable=False) 
    gravity = Column(Float, nullable=False) 
    climate = Column(String(250), nullable=False)

class Planets_Fav(Base):
    __tablename__ = "planets_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    user_to = relationship("users",foreign_keys=[user_id])
    planet_id = Column(Integer, ForeignKey("planets.id")) 
    planet_fav = relationship("planets",foreign_keys=[planet_id])


class StarShips(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    speed = Column (Float, nullable=False) 
    passenger = Column(Integer, nullable=False) 
    model = Column(String(250), nullable=False) 
    capacity = Column(Float, nullable=False)

class StarShips_Fav(Base):
    __tablename__ = "starships_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    user_to = relationship("users",foreign_keys=[user_id])
    starship_id = Column(Integer, ForeignKey("starships.id")) 
    starship_fav = relationship("starships",foreign_keys=[starship_id])


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
