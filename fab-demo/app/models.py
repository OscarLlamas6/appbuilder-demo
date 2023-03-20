from datetime import datetime
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Boolean
from flask_appbuilder.models.decorators import renders
from sqlalchemy.orm import relationship
from flask import Markup, url_for, redirect
from . import db

# Creating models
class Empleado(Model):
    __table_args__ = {"schema": "flaskdb"}
    __tablename__ = "empleado"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstName = Column(String(100), unique=False, nullable=False)
    lastName = Column(String(100),unique=False, nullable=False)
    birthDate = Column(DateTime, unique=False, nullable=False)

    def __repr__(self):
        return self.username
    
    def listartareas(self):
        tareas=""
        #return self.tareas
        for tarea in self.tareas:
            tareas += str(tarea) + "<br>"
        return Markup(tareas)
    
class Tarea(Model):
    __table_args__ = {"schema": "flaskdb"}
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)
    task_name = Column(String(180), unique=False, nullable=False)
    started = Column(Boolean, default=True)
    finished = Column(Boolean, default=False)
    begin_date = Column(Date, unique=False, default=datetime.now())
    end_date = Column(Date, unique=False)
    empleado_id = Column(Integer, ForeignKey('flaskdb.empleado.id'))
    empleado = relationship("Empleado", backref='tareas')

    def __repr__(self):
        return self.task_name

    @renders('started')
    def estadorender(self):
        if self.started and self.finished is False:
            return Markup('<b> En proceso </b>')
        return Markup('<b> Finalizado </b>')
    
    @renders('end_date')
    def enddaterender(self):
        if self.end_date is None:
            return Markup('<b> - </b>')
        return Markup('<b>' + str(self.end_date)  + '</b>')

db.create_all()