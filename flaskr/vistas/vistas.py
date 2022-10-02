from flask import request
from ..modelos import db, Usuario, UsuarioSchema, UbicacionSchema, Ubicacion
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
import time
usuario_schema = UsuarioSchema()
ubicacion_schema = UbicacionSchema()

class VistaUbicaciones(Resource):
    @jwt_required()
    def get(self):
        print(Ubicacion.query.filter())
        return [ubicacion_schema.dump(ubicacion)
                        for ubicacion in Ubicacion.query.filter()]