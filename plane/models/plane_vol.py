from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Char('passatgers')
    datasortida = fields.Datetime('datasortida')
    dataArrivada = fields.Datetime('datasortida')