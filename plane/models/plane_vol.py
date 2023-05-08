from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Char('passatgers')
    datasortida = fields.Date('datasortida')
    dataArrivada = fields.Date('datasortida')