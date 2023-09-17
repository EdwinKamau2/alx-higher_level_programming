#!/usr/bin/python3
""" This is a Module that defines State class representing 'states' table """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class linked to 'states' table

    attrs:
    id (int): primary key, auto-generated, unique
    name (str): max 128 chars
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
