from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import *


#Create your Model based REST API::
class MyEmpleadoApi(ModelRestApi):
    datamodel = SQLAInterface(Empleado)
appbuilder.add_api(MyEmpleadoApi)


# Create your Views::
class MyEmpleadoView(ModelView):
    datamodel = SQLAInterface(Empleado)
    label_columns = {
        "username": "Nombre de usuario",
        "firstName": "Nombre",
        "lastName": "Apellido",
        "birthDate": "Fecha de nacimiento",
    }
    description_columns = {
        "username": "your models name column"
    }
    edit_columns = ["firstName", "lastName"]
    list_columns = ["username", "firstName", "lastName", "birthDate"]


#Next, register your Views::
appbuilder.add_view(
    MyEmpleadoView,
    "Empleado",
    icon="fa-folder-open-o",
    category="My Category",
    category_icon='fa-envelope'
)


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