from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    imatge = fields.Char('Imatge')
    marca = fields.Char('marca')
    model = fields.Integer('model')
    maxvel = fields.Float('maxvel')
