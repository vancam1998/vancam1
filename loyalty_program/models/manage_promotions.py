from odoo import fields, models, api


class ManagePromotions(models.Model):
    _name = 'manage.promotions'
    _description = 'Description'

    name = fields.Text('loyalty program Name: ')
    points = fields.Float('% points: ')
    active = fields.Boolean('Active: ', required=True, default=True)



