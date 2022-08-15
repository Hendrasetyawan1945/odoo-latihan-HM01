from odoo import fields, models, api


class penyelenggara(models.Model):
    _inherit = 'res.partner'
    _description = 'Description'
    
    is_tutor = fields.Boolean(
        string='Tutor kursusku',
        required=False)
    is_admin = fields.Boolean(
        string='Admin kursusku',
        required=False)
    is_keterangan = fields.Boolean(
        string='Keterangan status peserta kursusku',
        required=False)

    kursuskita = fields.Many2one(
        comodel_name='kursusku.sesioninggris',
        string='Kursus',
        required=False)


