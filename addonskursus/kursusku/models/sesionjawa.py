from odoo import fields, models, api


class sesionjawa(models.Model):
    _name = 'kursusku.sesionjawa'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.python',
        string='Nama_kursus',
        required=False)

    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
        required=False,
        domain=[('function', '=', 'Bahasa')])


    tgl_mulai= fields.Datetime(
        string='Tanggal mulai',
        required=False,
         default=fields.Datetime.now()
     )

    peserta_jawa_ids = fields.One2many(
        comodel_name='kursusku.pesertajawa',
        inverse_name='sesionjawa_id',
        string='Peserta Jawa IDS',
        required=False)
    jum_siswa = fields.Integer(
        compute='_compute_siswa',
        string='Jumplah Siswa',
        required=False)


    @api.model
    def _compute_siswa(self):
        for i in self: #mapped = mengambil
            a = self.env['kursusku.pesertajawa'].search([('sesionjawa_id', '=', i.id)]).mapped('display_name')
            b = len(a)
            i.jum_siswa= b
            #menambah dari model python == untuk menghitung
            i.nama_kursus.jum_siswa = b



class pesertajawa(models.Model):
    _name = 'kursusku.pesertajawa'
    _description = 'peserta pemerograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemrograman',
        required=False,
        domain=[('is_peserta', '=', True), ('kategori_pilihan', '=', 'bahasa')])

    sesionjawa_id = fields.Many2one(
        comodel_name='kursusku.sesionjawa',
        string='Session Jawa id',
        required=False)