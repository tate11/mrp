# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MrpProduction(models.Model):

    _inherit = 'mrp.production'

    @api.multi
    def _get_materials_warning_visible(self):
        ''' Helper field that formulates the same condition that shows/hides the 'Raw materials missing!'
        label in the form view. We can then add this condition for hiding the Produce buttons '''
        for production in self:
            if production.state in ['confirmed', 'progress'] and production.availability not in ['assigned', 'none']:
                production.materials_warning_visible = True
            else:
                production.materials_warning_visible = False

    materials_warning_visible = fields.Boolean(compute=_get_materials_warning_visible, string='Raw Materials Warning Shown')