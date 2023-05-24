from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    grandaria = fields.Integer('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('ciutat')
    pais = fields.Char('Pais')

    animal_ids = fields.One2many('zoo.animal', 'zoo_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom)