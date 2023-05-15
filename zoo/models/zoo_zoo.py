from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    grandaria = fields.Integer('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('ciutat')
    pais = fields.Char('Pais')