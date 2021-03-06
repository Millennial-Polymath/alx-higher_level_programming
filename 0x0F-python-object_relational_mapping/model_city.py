#!/usr/bin/python3
"""
Contains class definition of a city
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
