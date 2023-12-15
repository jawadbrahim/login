from dataclasses import dataclass
import datetime
import uuid

@dataclass
class UserDataClass:
    id=uuid.UUID
    username=str
    password=str
    create_at=datetime