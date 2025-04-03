from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base, engine


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    is_completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
