from odoo import models, fields, api

class HideButtonRule(models.Model):
    _name = 'hide.button.rule'
    _description = 'Hide Button Rules'

    name = fields.Char(string='Rule Name', required=True)
    button_name = fields.Char(string='Button Name', required=True, help='Name of the button to hide')
    model_name = fields.Char(string='Object', required=True, help='Model name e.g., purchase.order')
    method_name = fields.Char(string='Method', help='Method called by the button')
    user_ids = fields.Many2many(
        'res.users',
        string='Applied Users',
        help='Users who will not see this button'
    )
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_button_rule', 'unique(button_name, model_name, method_name)',
         'Rule for this button already exists!'),
    ]

    @api.model
    def get_hidden_buttons_for_user(self, user_id):
        rules = self.sudo().search([
            ('active', '=', True),
            ('user_ids', 'in', [user_id])
        ])
        hidden_buttons = []
        for rule in rules:
            hidden_buttons.append({
                'button_name': rule.button_name,
                'model_name': rule.model_name,
                'method_name': rule.method_name,
            })
        return hidden_buttons
