# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, models


class BaseModelExtension(models.AbstractModel):
    """
    Abstract model providing button hiding functionality for any model.
    """
    _name = 'base.model.extension'
    _description = 'Base Model Extension for Button Hiding'

    @api.model
    def _is_button_hidden_for_user(self, button_name, model_name=None):
        """
        Check if a specific button should be hidden for the current user.

        :param button_name: The technical name of the button
        :param model_name: The model name (defaults to self._name)
        :return: True if the button should be hidden, False otherwise
        """
        if model_name is None:
            model_name = self._name

        # Find buttons that match the criteria and check if current user is restricted
        buttons = self.env['itcustom.button'].search([
            ('model', '=', model_name),
            ('button_name', '=', button_name),
            ('active', '=', True),
        ])

        for button in buttons:
            if self.env.user in button.restrict_user_ids:
                return True

        return False
