from odoo import fields, models, api


class sesionpy(models.Model):
    _name = 'kursusku.sesionpy'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.python',
        string='Nama_kursus',
        required=False)
    tgl_mulai= fields.Datetime(
        string='Tanggal mulai',
        required=False,
         default=fields.Datetime.now()
     )

    peserta_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='kursus',
        string='Peserta_ids',
        required=False)