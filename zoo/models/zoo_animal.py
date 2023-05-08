from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animals'
    id = fields.Integer('Id', required=True)
    continentorigen = fields.Char('Continent Origen')
    datanaix = fields.Date('Data Naix')
    paisorigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')