from odoo import fields, models, api


class kerangankursus(models.Model):
    _name = 'keterangankursus.keterangan'
    _description = 'Description'

    name = fields.Char(string='Diskripsi kursus')
    harga = fields.Integer(String='harga',required=True)
    keterangan = fields.Selection(string='keterangan',
                                  selection=[('dasar', 'Dasar'), ('menegah', 'Menengah'), ('kakap', 'Kakap')],
                                  required=True)
    kelas_ids = fields.One2many(
        comodel_name='kursusku.kursus',
        inverse_name='tingkatan',
        string='Kelas id',
        required=False)
