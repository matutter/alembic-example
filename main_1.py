from db import *
from models import *
from sqlalchemy.orm import sessionmaker

print(connect_string)

session = sessionmaker(bind=engine)()
for name in ('A', 'B', 'C'):
  session.add(UserModel(name=name, role='user'))
session.commit()

user_count = session.query(UserModel).count()
print(f'There are {user_count} users')
