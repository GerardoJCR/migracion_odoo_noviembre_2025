from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_latam_document_code = fields.Char(
        related='l10n_latam_document_type_id.code',
        string='Código Documento'
    )
    l10n_latam_internal_type = fields.Selection(
        related='l10n_latam_document_type_id.internal_type',
        string='Tipo de Documento Interno',
        readonly=True
    )