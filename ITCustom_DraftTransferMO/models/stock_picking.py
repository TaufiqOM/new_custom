from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)
        if picking.state == 'draft' and picking.origin and picking.origin.startswith('PROD '):
            picking.name = f"Draft {picking.origin}"
        return picking
