from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'libreria.cliente'
    id = fields.Char(string='Id', required=True)
    nombre = fields.Char(string='Nombre del cliente', required=True)
    apellido = fields.Char(string='Apellidos del cliente', required=True)
    telefono = fields.Char(string='Telefono del cliente')

    def limpiar_todo(self):
        self.write({
            'id': '',
            'nombre': '',
            'apellido': '',
            'telefono': ''
        })

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res