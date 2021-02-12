from odoo import models, fields, api


class Categoria(models.Model):
    _name = 'libreria.categoria'
    tipo = fields.Char(string='Nombre de la categoria', required=True)

    def limpiar_todo(self):
        self.write({
            'tipo': ''
        })

    def name_get(self):
        res = []
        for record in self:
            name = record.tipo
            res.append((record.id,name))
        return res