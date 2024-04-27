from sqlalchemy import INTEGER
from sqlalchemy.orm import mapped_column

from models.Base import Base


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(INTEGER(), primary_key=True)
