import os

class Config:
    """Base configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///instance/database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
