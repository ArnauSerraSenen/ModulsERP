from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    pais = fields.Char('Pais ')
    latitud = fields.Integer('Latitud')
    longitud = fields.Integer('Longitud')
