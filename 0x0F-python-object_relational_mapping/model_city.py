#!/usr/bin/python3
""" Write Python file similar to contain class definition of City """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ You must use the module SQLAlchemy """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
