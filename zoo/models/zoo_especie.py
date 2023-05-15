from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    familia = fields.Char('Familia')
    nomcientific = fields.Char('Nom Cientific')
    nomvulgar = fields.Char('Nom Vulgar')
    perill = fields.Char('Perill')