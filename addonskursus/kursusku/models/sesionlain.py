from odoo import fields, models, api


class sesionlain(models.Model):
    _name = 'kursusku.sesionlain'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.bahasalain',
        string='Nama kursus',
        required=False,
    )
    tgl_mulai= fields.Datetime(
        string='Tanggal mulai',
        required=False,
         default=fields.Datetime.now()
     )
    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama Tutor',
        required=False,
        domain=[('function', '=', 'Umum')])

    peserta_pemrograman_ids = fields.One2many(
        comodel_name='kursusku.pesertalain',
        inverse_name='sesionlain_ids',
        string='Peserta Lain-lain IDS',
        required=False)

    jum_siswa = fields.Integer(
        compute='_compute_siswa',
        string='Jumplah Siswa',
        required=False)

    @api.model
    def _compute_siswa(self):
        for i in self:  # mapped = mengambil
            a = self.env['kursusku.pesertalain'].search([('sesionlain_ids', '=', i.id)]).mapped('display_name')
            b = len(a)
            i.jum_siswa = b
            # menambah dari model Lain-lain == untuk menghitung
            i.nama_kursus.jum_siswa_bing = b

class pesertalain(models.Model):
    _name = 'kursusku.pesertalain'
    _description = 'peserta lain lain'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Lain-lain',
        required=False,
        domain=[('is_peserta', '=', True), ('kategori_pilihan', '=', 'umum')])
    sesionlain_ids = fields.Many2one(
        comodel_name='kursusku.sesionlain',
        string='Session Lain-lain id',
        required=False)

    # domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'pemrograman')])
    # domain=[('is_peserta', '=', True) and ('kategori_pilihan', '=', 'Teknologi')]
    # domaian=[('is_peserta', '=', True)] and [('kategori_pilihan', '=', 'Teknologi')]

