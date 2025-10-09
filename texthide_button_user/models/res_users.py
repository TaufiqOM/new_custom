from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    hide_button_rule_ids = fields.Many2many(
        'hide.button.rule',
        'hide_button_rule_user_rel',
        'user_id',
        'rule_id',
        string='Hidden Button Rules'
    )
