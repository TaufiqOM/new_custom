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
from odoo import models, fields


class PurchaseOrder(models.Model):
    """
    Model to extend purchase.order for hiding buttons based on user.
    """
    _inherit = 'purchase.order'

    def _compute_hide_confirm_button(self):
        """
        Compute method to check if the Confirm Order button should be hidden for the current user.
        """
        for record in self:
            record.hide_confirm_button = bool(
                self.env.user.hide_button_ids.filtered(
                    lambda b: b.model == 'purchase.order' and b.button_name == 'button_confirm_manual'
                )
            )

    hide_confirm_button = fields.Boolean(
        compute='_compute_hide_confirm_button',
        string='Hide Confirm Button',
        help='Whether to hide the Confirm Order button for the current user.'
    )
