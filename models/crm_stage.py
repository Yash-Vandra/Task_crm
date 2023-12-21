from odoo import models, fields

class MyCrmStage(models.Model):
    _inherit = 'crm.stage'
    is_quotation_ready = fields.Boolean("Is Quotation Ready?")