from typing import Optional, List
from pydantic import BaseModel, ValidationError

class Auth_key(BaseModel):
    key: str

class Pet(BaseModel):
    age: Optional[int]
    animal_type: Optional[str]
    created_at: Optional[str]
    id: Optional[str]
    name: Optional[str]
    pet_photo: Optional[str]



class Pets(BaseModel):
    pets: Optional[List[Pet]]
