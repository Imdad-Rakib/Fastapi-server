from pydantic import BaseModel

class ExampleCreate(BaseModel):
    name: str
    description: str

class ExampleRead(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

class ExampleUpdate(BaseModel):
    name: str = None
    description: str = None