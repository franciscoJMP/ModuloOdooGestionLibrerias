from odoo import models, fields, api


class Libro(models.Model):
    _name = 'libreria.libro'
    id = fields.Char(string='Id', required=True)
    nombre = fields.Char(string='Nombre del libro', required=True)
    autor = fields.Char(string='Autor del libro', required=True)
    imagen = fields.Binary(string='Foto')
    categoria = fields.Many2many('libreria.categoria', string='Categoria')
    cliente = fields.Many2one('libreria.cliente', string='Cliente')
    descripcion = fields.Html(string='Descripcion')

    def limpiar_todo(self):
        self.write({
            'id': '',
            'nombre': '',
            'autor': '',
            'categoria': '',
            'cliente': '',
            'descripcion': ''
        })

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id,name))
        return res