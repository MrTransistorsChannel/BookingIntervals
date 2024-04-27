from datetime import datetime, timedelta

from models import database
from models.Base import Base
from models.User import User
from models.Table import Table
from models.BookedInterval import BookedInterval
from models.database import db


def getFreeBookingIntervals(starts_at=datetime.strptime("0001-01-01 12:30:00", "%Y-%m-%d %H:%M:%S"),
                            ends_at=datetime.strptime("0001-01-01 12:40:00", "%Y-%m-%d %H:%M:%S")):
    booked_intervals = db.query(BookedInterval).filter_by(table_id=1) \
        .filter(BookedInterval.ends_at > starts_at) \
        .filter(BookedInterval.starts_at < ends_at) \
        .order_by(BookedInterval.starts_at) \
        .all()

    free_intervals = []
    interval_start = starts_at

    for interval in booked_intervals:
        if interval.starts_at > interval_start:
            free_intervals.append((interval_start, interval.starts_at))
        interval_start = interval.ends_at

    if ends_at > interval_start:
        free_intervals.append((interval_start, ends_at))

    print('\nBooked at:')
    for booked_interval in booked_intervals:
        start_time_str = booked_interval.starts_at.strftime("%Y-%m-%d %H:%M:%S")  # Format start time
        end_time_str = booked_interval.ends_at.strftime("%Y-%m-%d %H:%M:%S")  # Format end time
        print(f"ID: {booked_interval.id}, Start Time: {start_time_str}, End Time: {end_time_str}")

    print('\nFree at:')
    for free_interval in free_intervals:
        start_time_str = free_interval[0].strftime("%Y-%m-%d %H:%M:%S")  # Format start time
        end_time_str = free_interval[1].strftime("%Y-%m-%d %H:%M:%S")  # Format end time
        print(f"Start Time: {start_time_str}, End Time: {end_time_str}")

if __name__ == '__main__':
    Base.metadata.drop_all(database.engine)
    Base.metadata.create_all(database.engine)

    db.add(User())
    db.add(Table())

    db.add(BookedInterval(user_id=1,
                          table_id=1,
                          starts_at=datetime.strptime("0001-01-01 12:30:00", "%Y-%m-%d %H:%M:%S"),
                          ends_at=datetime.strptime("0001-01-01 13:30:00", "%Y-%m-%d %H:%M:%S"))
           )

    db.add(BookedInterval(user_id=1,
                          table_id=1,
                          starts_at=datetime.strptime("0001-01-01 11:30:00", "%Y-%m-%d %H:%M:%S"),
                          ends_at=datetime.strptime("0001-01-01 12:10:00", "%Y-%m-%d %H:%M:%S"))
           )

    db.add(BookedInterval(user_id=1,
                          table_id=1,
                          starts_at=datetime.strptime("0001-01-01 15:00:00", "%Y-%m-%d %H:%M:%S"),
                          ends_at=datetime.strptime("0001-01-01 17:00:00", "%Y-%m-%d %H:%M:%S"))
           )

    db.commit()

    getFreeBookingIntervals()
