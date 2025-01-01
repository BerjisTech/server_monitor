import os

class Config:
    """Base configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql://caller_sim2:caller_sim2_password@caller-db:5432/server_monitor_db"  # Fallback value
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")

