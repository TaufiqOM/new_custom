from odoo import http
from odoo.http import request

class HideButtonController(http.Controller):
    
    @http.route('/hide_button/get_hidden_buttons', type='json', auth='user')
    def get_hidden_buttons(self):
        user_id = request.env.user.id
        rules = request.env['hide.button.rule'].sudo().search([
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
