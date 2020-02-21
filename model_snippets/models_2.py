
class AdminModel(UserModel):
  __tablename__   = 'admin'
  __mapper_args__ = { 'polymorphic_identity': 'admin' }
  _id = Column(Integer, ForeignKey('user._id'), primary_key=True)
  admin_secret = Column(String(30), default=token_hex(6))
