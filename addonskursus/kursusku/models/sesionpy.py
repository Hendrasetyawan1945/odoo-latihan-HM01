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
        required=False,
        domain=[('function', '=', 'Pemerograman')])


    tgl_mulai= fields.Datetime(
        string='Tanggal mulai',
        required=False,
         default=fields.Datetime.now()
     )

    peserta_pemrograman_ids = fields.One2many(
        comodel_name='kursusku.pesertapemerograman',
        inverse_name='sesionpy_ids',
        string='Peserta Pemerograman IDS',
        required=False)
    jum_siswa = fields.Integer(
        compute='_compute_siswa',
        string='Jumplah Siswa',
        required=False)


    @api.model
    def _compute_siswa(self):
        for i in self: #mapped = mengambil
            a = self.env['kursusku.pesertapemerograman'].search([('sesionpy_ids', '=', i.id)]).mapped('display_name')
            b = len(a)
            i.jum_siswa= b
            #menambah dari model python == untuk menghitung
            i.nama_kursus.jum_siswa_prog = b




class pesertapemerograman(models.Model):
    _name = 'kursusku.pesertapemerograman'
    _description = 'peserta pemerograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemrograman',
        required=False,
        domain=[('is_peserta', '=', True), ('kategori_pilihan', '=', 'teknologi')])

    # domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'pemrograman')])
    # domain=[('is_peserta', '=', True) and ('kategori_pilihan', '=', 'Teknologi')]
    # domaian=[('is_peserta', '=', True)] and [('kategori_pilihan', '=', 'Teknologi')]

    sesionpy_ids = fields.Many2one(
        comodel_name='kursusku.sesionpy',
        string='Session Python id',
        required=False)