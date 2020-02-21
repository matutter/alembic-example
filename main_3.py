from main_2 import *

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()
for name in ('A', 'B', 'C'):
  session.add(SuperAdminModel(name=f'SU-ADMIN-{name}'))
session.commit()

user_count = session.query(UserModel).filter(UserModel.role=='superadmin').count()
print(f'There are {user_count} super-admins')
