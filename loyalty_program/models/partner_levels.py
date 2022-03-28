from odoo import fields, models, api


class Partnerlevels (models.Model):
    _name = 'partner.levels'
    _description = 'Description'

    name = fields.Char(string='Partner level')
    loyalty_points = fields.Float('Loyalty Points')
    description = fields.Text('Description')
