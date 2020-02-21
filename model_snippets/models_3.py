
class SuperAdminModel(AdminModel):
  __tablename__   = 'superadmin'
  __mapper_args__ = { 'polymorphic_identity': 'superadmin' }
  _id = Column(Integer, ForeignKey('admin._id'), primary_key=True)
  super_secret = Column(String(30), default=token_hex(6))
