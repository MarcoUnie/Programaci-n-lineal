from database import Base
from sqlalchemy import Column, Integer, String

class RecursoBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    cantidad = Column(Integer, nullable=False)
