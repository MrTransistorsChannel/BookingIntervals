from sqlalchemy import INTEGER, ForeignKey, DATETIME
from sqlalchemy.orm import mapped_column, relationship

from models.Base import Base


class BookedInterval(Base):
    __tablename__ = 'booking_intervals'

    id = mapped_column(INTEGER(), primary_key=True)
    user_id = mapped_column(ForeignKey('users.id'))
    table_id = mapped_column(ForeignKey('tables.id'))
    starts_at = mapped_column(DATETIME())
    ends_at = mapped_column(DATETIME())

    user = relationship('User', foreign_keys=[user_id])
    table = relationship('Table', foreign_keys=[table_id])
