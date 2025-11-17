from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_latam_exchange_rate = fields.Float(
        string='Tipo de Cambio',
        digits=0,
        compute='_compute_l10n_pe_currency_rate',
        store=True
    )

    @api.depends('currency_id', 'company_id', 'amount_total', 'amount_total_in_currency_signed')
    def _compute_l10n_pe_currency_rate(self):
        for move in self:
            if move.move_type in ('out_invoice','out_refund','in_invoice','in_refund'):
                move.l10n_latam_exchange_rate = move._get_actual_currency_rate()

    def _get_actual_currency_rate(self):
        if not self.currency_id:
            return 1.0
        
        currency_rate_tmp = abs(self.amount_total_signed/self.amount_total_in_currency_signed) if self.amount_total_in_currency_signed!=0 else 1
        return currency_rate_tmp
