from sqlalchemy import ForeignKey, String, Boolean, Column, Integer, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from secrets import token_hex

Base = declarative_base()

class UserModel(Base):
  __tablename__ = 'user'
  _id     = Column(Integer, primary_key=True)
  role    = Column(String, nullable=False)
  name    = Column(String)
  enabled = Column(Boolean)

  __mapper_args__ = {
    'polymorphic_identity': 'user',
    'polymorphic_on': 'role'
  }

  def __repr__(self):
    return f'{self.role.capitalize()}({self.name}, enabled={self.enabled})'

class AdminModel(UserModel):
  __tablename__   = 'admin'
  __mapper_args__ = { 'polymorphic_identity': 'admin' }
  _id = Column(Integer, ForeignKey('user._id'), primary_key=True)
  admin_secret = Column(String(30), default=token_hex(6))

class SuperAdminModel(AdminModel):
  __tablename__   = 'superadmin'
  __mapper_args__ = { 'polymorphic_identity': 'superadmin' }
  _id = Column(Integer, ForeignKey('admin._id'), primary_key=True)
  super_secret = Column(String(30), default=token_hex(6))
