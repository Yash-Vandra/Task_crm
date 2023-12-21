from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendor_type_id = fields.Many2one('res.partner.vendor.type',string="Vendor Type")