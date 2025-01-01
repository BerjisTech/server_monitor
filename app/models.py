from .extensions import db

class Server(db.Model):
    """Model for monitored servers."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False, unique=True)
    status = db.Column(db.String(50), default="unknown")  # e.g., 'online', 'offline'

    def to_dict(self):
        """Convert server instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "ip_address": self.ip_address,
            "status": self.status,
        }
