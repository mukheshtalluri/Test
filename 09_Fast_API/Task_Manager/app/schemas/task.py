from pydantic import BaseModel

class TaskBase(BaseModel):
    title : str
    description : str

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id : int
    owner_id : int
    completed : bool

    class Config:
        orm_mode = True

