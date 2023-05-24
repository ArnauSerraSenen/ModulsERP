from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Char('passatgers')
    datasortida = fields.Datetime('datasortida')
    dataArrivada = fields.Datetime('datasortida')
    desti = fields.Many2one('plane.aeroport', string='Desti')
    origen = fields.Many2one('plane.aeroport', string='Origen')
    avio_id = fields.Many2one('plane.avio', string='Avio')
    pilot_id = fields.Many2one('plane.pilot', string="Pilot")