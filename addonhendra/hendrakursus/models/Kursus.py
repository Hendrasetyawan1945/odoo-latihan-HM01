
from odoo import api, fields, models

class Kursus(models.Model):
    _name = 'kursusku.kursus'
    _description = 'Nama kategori'

    name = fields.Char(string='Daftar kursus')
    kategori= fields.Selection(string='kategori pembelajaran',selection=[('teknologi','Teknologi'),('umum','Umum'),('manufaktur','Manufaktur')],required=True)
    tingkatan = fields.Many2one(
        comodel_name='keterangankursus.keterangan',
        string='Diskripsi Belajar',
        required=False)
    tutor = fields.Many2one(
        comodel_name='pengajarku.pengajar',
        string='Pengajar',
        required=False)
