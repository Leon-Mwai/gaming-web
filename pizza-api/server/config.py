import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # or your DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
