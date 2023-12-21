from odoo import models, fields, api


class MyCrm(models.Model):
    _inherit = 'crm.lead'

    quote_status = fields.Selection(
        [('import_quote_requested', 'Import Quote Requested'),
         ('import_quote_ready', 'Import Quote Ready'),
         ('import_quote_submitted', 'Import Quote Submitted'),
         ('import_quote_revision_requested', 'Import Quote Revision Requested')],
        string='Import Quote Status',
        copy=False)
    domestic_quote_status = fields.Selection(
        [('domestic_quote_requested', 'Domestic Quote Requested'),
         ('domestic_quote_ready', 'Domestic Quote Ready'),
         ('domestic_quote_submitted', 'Domestic Quote Submitted'),
         ('domestic_quote_revision_requested', 'Domestic Quote Revision Requested')],
        string='Domestic Quote Status',
        copy=False)

    @api.onchange('quote_status', 'domestic_quote_status')
    def _onchange_status(self):
        if (self.quote_status == 'import_quote_ready') and (self.domestic_quote_status == False):
            self.stage_id = self.env['crm.stage'].search([('name', '=', 'Quote ready')])
        elif ((self.quote_status == False) and (self.domestic_quote_status == 'domestic_quote_ready')):
            self.stage_id = self.env['crm.stage'].search([('is_quotation_ready', '=', True)])
        elif ((self.quote_status == 'import_quote_ready') and (self.domestic_quote_status == 'domestic_quote_ready')):
            self.stage_id = self.env['crm.stage'].search([('is_quotation_ready', '=', True)])



