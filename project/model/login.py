from database.postgres import sqlalchemy_db as db
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID
from dataclasses import dataclass

@dataclass
class UserStatus:
 ACTIVE="ACTIVE"
 DELETED="DELETED"

class Login(db.Model):
 id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
 email=db.Column(db.String,nullable=False)
 password=db.Column(db.String,nullable=False)
 login_at=db.Column(db.DateTime,default=datetime.datetime.utcnow())

