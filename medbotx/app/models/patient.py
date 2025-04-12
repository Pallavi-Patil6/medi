from pydantic import BaseModel
from typing import List

class PatientInput(BaseModel):
    name: str
    age: int
    symptoms: List[str]
