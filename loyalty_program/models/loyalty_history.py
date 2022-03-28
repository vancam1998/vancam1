from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Description'

    order_code = fields.Char('Mã đơn hàng')

    partner_id = fields.Many2one(comodel_name='manage.promotions', string='Tên chương trình khuyến mãi')
    loyalty_points = fields.Float(string='Tổng số điểm tích lũy nhận được trong 1 đơn hàng', compute='_get_points')
    money_spent = fields.Float('Tổng tiền của 1 đơn hàng')
    loyalty_point = fields.Float('Số điểm đã tích lũy của khách hàng', readonly=True)
    date_order = fields.Datetime(string='Thời gian xác nhận đơn hàng', required=True, readonly=True, copy=False,
                                 default=fields.Datetime.now)

    product_id = fields.Many2one('product.product', string='Product',
                                 change_default=True, ondelete='restrict')  # Unrequired company
    # customer_id = fields.Many2one(comodel_name='res.partner', string='Tên khách hàng')
    # product_price = fields.Float('Giá sản phẩm',compute='_get_price_product')
    product_price = fields.Float(related='product_id.list_price', string='Giá sản phẩm', tracking=True)
    _points = fields.Float(related='partner_id.points')

    @api.depends('product_price')
    def _get_points(self):
        for rec in self:
            rec.loyalty_points = rec.product_price * rec._points / 100

