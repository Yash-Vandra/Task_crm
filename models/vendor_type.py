from odoo import models, fields


class VendorType(models.Model):
    _name = 'res.partner.vendor.type'

    name = fields.Char(string="Vendor Type")
    description = fields.Char(string="Description")
    active = fields.Boolean(default=True)