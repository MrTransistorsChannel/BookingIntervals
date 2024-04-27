from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.sqlite', echo=True)
db = sessionmaker(bind=engine).__call__()
