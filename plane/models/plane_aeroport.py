from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    pais = fields.Char('Pais ')
    latitud = fields.Integer('Latitud')
    longitud = fields.Integer('Longitud')
    vol_id_sortida = fields.One2many('plane.vol', 'origen', string='Vols de sortida')
    vol_id_entrada = fields.One2many('plane.vol', 'desti', string='Vols dentrada')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.pais)