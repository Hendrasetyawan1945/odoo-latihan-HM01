
from odoo import api, fields, models

class Kursus(models.Model):
    _name = 'kursusku.kursus'
    _description = 'Nama kategori'

    name = fields.Char(string='Daftar kursus')
    keterangan = fields.Selection(string='keterangan',
                             selection=[('dasar', 'Dasar'), ('menegah', 'Menengah'), ('kakap', 'Kakap')],
                             required=True)
    harga = fields.Integer(String='harga',required=True)
    kategori= fields.Selection(string='kategori pembelajaran',selection=[('teknologi','Teknologi'),('umum','Umum'),('manufaktur','Manufaktur')],required=True)


