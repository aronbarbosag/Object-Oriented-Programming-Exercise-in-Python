from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine('sqlite:///db_course.sqlite')
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)