from pydantic import BaseModel

class Auth_key(BaseModel):
    key: str

class Pets(BaseModel):
    age: int
    animal_type: str
    created_at: str
    id: str
    name: str
    pet_photo: str
    user_id: str