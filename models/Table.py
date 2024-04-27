from sqlalchemy import INTEGER
from sqlalchemy.orm import mapped_column

from models.Base import Base


class Table(Base):
    __tablename__ = 'tables'

    id = mapped_column(INTEGER(), primary_key=True)
