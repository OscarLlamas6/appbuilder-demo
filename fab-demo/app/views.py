from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access

from . import appbuilder, db
from .models import *

# Creating BaseViews
class VistaBase(BaseView):
    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        param1 = "Hola Mundo :D" 
        return self.render_template('view1.html', param1=param1)
    
appbuilder.add_view(VistaBase, 'Method1', category='My View')


# Create your Model based REST API:
class MyTareaApi(ModelRestApi):
    datamodel = SQLAInterface(Tarea)
appbuilder.add_api(MyTareaApi)

class MyEmpleadoApi(ModelRestApi):
    datamodel = SQLAInterface(Empleado)
appbuilder.add_api(MyEmpleadoApi)


# Create your Views:
class MyTareaModelView(ModelView):
    datamodel = SQLAInterface(Tarea)
    add_exclude_columns = ["begin_date", "end_date"]
    label_columns = { 'estadorender': 'Status',
                      'enddaterender' : 'End Date',
                      'begin_date': 'Begin Date',
                    }
    list_columns = ['estadorender', 'task_name', 'empleado', 'begin_date', 'enddaterender']

class MyEmpleadoView(ModelView):
    datamodel = SQLAInterface(Empleado)
    label_columns = {
        "username": "Nombre de usuario",
        "firstName": "Nombre",
        "lastName": "Apellido",
        "birthDate": "Fecha de nacimiento",
        "listartareas": "Tareas" 
    }
    description_columns = {
        "username": "your models name column"
    }
    edit_columns = ["firstName", "lastName"]
    list_columns = ["username", "firstName", "lastName", "birthDate", "listartareas"]
    search_exclude_columns = ["lastName"]
    related_views = [MyTareaModelView]

# Next, register your Views:
appbuilder.add_view(
    MyEmpleadoView,
    "Empleado",
    icon="fa-folder-open-o",
    category="My Category",
    category_icon='fa-envelope'
)

appbuilder.add_view_no_menu(MyTareaModelView)

# Application wide 404 error handler
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()