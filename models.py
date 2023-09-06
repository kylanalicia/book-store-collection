#!/usr/bin/env python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLAlchemy engine and session connected to an SQLite database
engine = create_engine('sqlite:///data/books.db')