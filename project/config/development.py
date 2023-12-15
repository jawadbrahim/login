import os
from dataclasses import dataclass
@dataclass
class Development:
 DATABASE_URI=os.getenv("DATABASE_URI")
 MONGO_NAME=os.getenv("MONGO_NAME")
 MONGO_DATABASE_URI=os.getenv("MONGO_DATABASE_URI")