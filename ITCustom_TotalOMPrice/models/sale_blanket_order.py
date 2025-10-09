from odoo import models, fields, api

class SaleBlanketOrder(models.Model):
    _inherit = "sale.blanket.order"

    amount_total_sec_price = fields.Monetary(
        string="Total OM Price",
        compute="_compute_amount_total_sec_price",
        store=True,
    )

    @api.depends("line_ids.total_sec_price")
    def _compute_amount_total_sec_price(self):
        for order in self:
            order.amount_total_sec_price = sum(line.total_sec_price for line in order.line_ids)
