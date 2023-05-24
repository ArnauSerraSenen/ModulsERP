from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom Cientific')
    nomvulgar = fields.Char('Nom Vulgar')
    perill = fields.Char('Perill')
    animal_ids = fields.One2many('zoo.animal', 'especie_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomvulgar) + " " + str(record.familia)