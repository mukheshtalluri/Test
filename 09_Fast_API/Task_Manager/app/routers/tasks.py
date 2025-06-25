from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskOut
from app.crud import task as crud_task
from app.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud_task.create_task(db, task, user.id)

@router.get("/", response_model=list[TaskOut])
def read(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud_task.get_tasks(db, user.id)