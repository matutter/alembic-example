from db import *
from models import *
from sqlalchemy.orm import sessionmaker

print(connect_string)

Base.metadata.create_all(engine)
