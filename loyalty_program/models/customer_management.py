from odoo import fields, models, api


class CustomerManagement(models.Model):
    _inherit = 'res.partner' #không cần hàm này
    # _name = 'customer.management'
    _description = 'customer_management'

    # hàm kế thừa res.partner
    # name = fields.Many2one(comodel_name='res.partner')
    loyalty_point = fields.Float('points_customer')
    loyalty_level = fields.Many2one(comodel_name='partner.levels', string='cấp độ của khách hàng')

