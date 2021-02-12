from odoo import models, fields, api


class Librero(models.Model):
    _name = 'libreria.librero'
    id = fields.Char(string='Id', required=True)
    nombre = fields.Char(string='Nombre del librero', required=True)
    apellido = fields.Char(string='Apellidos del librero')
    fecha_venta = fields.Date(string="Fecha Venta")
    libro = fields.Many2many('libreria.libro', string='Libro')

    def limpiar_todo(self):
        self.write({
            'id': '',
            'nombre': '',
            'apellido': '',
            'fecha_venta': ''
        })

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id,name))
        return res