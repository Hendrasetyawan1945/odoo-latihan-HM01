from odoo import fields, models, api


class peserta(models.Model):
    _inherit = 'res.partner'
    _description = 'Description Raden Hendra Kertapati'

    kategori_pilihan = fields.Selection(
        string='Kategori Pembelajaran',
        selection=[('teknologi', 'Teknologi'), ('umum', 'Umum'), ('bahasa', 'Bahasa')],
        required=False)
    is_peserta = fields.Boolean(
        string='Is_peserta',
        required=False)

    kursus = fields.Many2one(
        comodel_name='kursusku.sesionpy',
        string='Kursus',
        required=False)
    kursusbing = fields.Many2one(
        comodel_name='kursusku.sesioninggris',
        string='Kursus bahasa ingggris',
        required=False)
    kursuslain = fields.Many2one(
        comodel_name='kursusku.sesionlain',
        string='Kursus Lain-lain',
        required=False)





