
from database.postgres import sqlalchemy_db as db

import uuid
import datetime
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class UserStatus:
    Active = 'Active'
    Deleted = 'Deleted'

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name= db.Column(db.String,nullable=False)
    last_name=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default=UserStatus.Active)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
