from odoo import fields, models, api


class LoyaltySale(models.Model):
    _inherit = 'sale.order'
    _description = 'Description'

    loyalty_program = fields.Many2one('manage.promotions')
    point = fields.Float(related='loyalty_program.points')
    points = fields.Float('point', compute="_get_points")


    @api.depends('point')
    def _get_points(self):
        for rec in self:
            rec.points = rec.point*(rec.amount_untaxed / 100)


