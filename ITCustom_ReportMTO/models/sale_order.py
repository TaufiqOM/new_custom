from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    production_time = fields.Integer(string="Production Time")
    confirmation_date_order = fields.Date(string="Confirmation Date Order")
    due_date_order = fields.Date(string="Due Date")
