from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from . import db

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who

"""

class Empleado(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstName = Column(String(100), unique=False, nullable=False)
    lastName = Column(String(100),unique=False, nullable=False)
    birthDate = Column(DateTime, unique=False, nullable=False)

    def __repr__(self):
        return self.username


db.create_all()