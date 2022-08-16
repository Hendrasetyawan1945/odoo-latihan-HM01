from odoo import fields, models, api


class sesionpy(models.Model):
    _name = 'kursusku.sesionpy'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.python',
        string='Nama_kursus',
        required=False)

    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
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

    peserta_pemerograman_ids = fields.One2many(
        comodel_name='kursusku.pesertapemerograman',
        inverse_name='sesionpy_ids',
        string='Peserta pemerograman ids',
        required=False)


class pesertapemerograman(models.Model):
    _name = 'kursusku.pesertapemerograman'
    _description = 'peserta pemerograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemerograman',
        required=False)

    sesionpy_ids = fields.Many2one(
        comodel_name='kursusku.sesionpy',
        string='Sesion Python ids',
        required=False)