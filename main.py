from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://admin2:4z7KhuPcOjJcgxck@hw4.rmddpcr.mongodb.net/?retryWrites=true&w=majority')