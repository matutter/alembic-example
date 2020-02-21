from main_1 import *

print(connect_string)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()
for name in ('A', 'B', 'C'):
  session.add(AdminModel(name=f'ADMIN-{name}'))
session.commit()

user_count = session.query(UserModel).filter(UserModel.role=='admin').count()
print(f'There are {user_count} admins')
