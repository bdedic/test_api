from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class User(BaseModel):
    id: UUID = uuid4()
    first_name: str
    last_name: str
    roles: List[Role]