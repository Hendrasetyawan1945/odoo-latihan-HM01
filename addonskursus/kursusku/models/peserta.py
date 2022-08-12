from odoo import fields, models, api


class peserta(models.Model):
    _inherit = 'res.partner'
    _description = 'Description Raden Hendra Kertapati'

    kategori_pilihan = fields.Selection(
        string='Kategori Pembelajaran',
        selection=[('teknologi', 'Teknologi'), ('umum', 'Umum')],
        required=False)


