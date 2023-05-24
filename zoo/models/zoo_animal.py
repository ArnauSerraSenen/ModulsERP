from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentorigen = fields.Char('Continent Origen')
    datanaix = fields.Date('Data Naix')
    paisorigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    especie_id = fields.Many2one('zoo.especie', string='Especie')