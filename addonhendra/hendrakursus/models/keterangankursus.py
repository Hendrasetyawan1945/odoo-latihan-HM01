from odoo import fields, models, api


class kerangankursus(models.Model):
    _name = 'keterangankursus.keterangan'
    _description = 'Description'

    name = fields.Char(string='Diskripsi kursus')
    harga = fields.Integer(String='harga',required=True)
    keterangan = fields.Selection(string='keterangan',
                                  selection=[('dasar', 'Dasar'), ('menegah', 'Menengah'), ('kakap', 'Kakap')],
                                  required=True)