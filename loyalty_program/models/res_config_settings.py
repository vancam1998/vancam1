from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    base_salary = fields.Integer("Email Notyfi")

    loyalty_email_notify = fields.Boolean('loyalty: ', default=True)

