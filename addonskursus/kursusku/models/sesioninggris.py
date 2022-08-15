from odoo import fields, models, api


class sesioinngris(models.Model):
    _name = 'kursusku.sesioninggris'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.inggris',
        string='Nama_kursus',
        required=False)

    tgl_mulai= fields.Datetime(
        string='Tanggal mulai',
        required=False,
         default=fields.Datetime.now()
     )

    pesertaa_idss = fields.One2many(
        comodel_name='res.partner',
        inverse_name='kursuskita',
        string='Peserta_ids',
        required=False)