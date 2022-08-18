from odoo import fields, models, api


class sesioinngris(models.Model):
    _name = 'kursusku.sesioninggris'
    _description = 'Description'

    nama_kursus = fields.Many2one(
        comodel_name='kursusku.inggris',
        string='Nama_kursus',
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
        domain=[('function', '=', 'Inggris')])

    peserta_pemrograman_ids = fields.One2many(
        comodel_name='kursusku.pesertabing',
        inverse_name='sesionbing_ids',
        string='Peserta Bahasa Inggris IDS',
        required=False)

    jum_siswa = fields.Integer(
        compute='_compute_siswa',
        string='Jumplah Siswa',
        required=False)

    @api.model
    def _compute_siswa(self):
        for i in self:  # mapped = mengambil
            a = self.env['kursusku.pesertabing'].search([('sesionbing_ids', '=', i.id)]).mapped('display_name')
            b = len(a)
            i.jum_siswa = b
            # menambah dari model inggris == untuk menghitung
            i.nama_kursus.jum_siswa_bing = b

class pesertabing(models.Model):
    _name = 'kursusku.pesertabing'
    _description = 'peserta pemerograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Bahasa Inggris',
        required=False,
        domain=[('is_admin', '=', True), ('kategori_pilihan', '=', 'umum')])
    sesionbing_ids = fields.Many2one(
        comodel_name='kursusku.inggris',
        string='Session Inggris id',
        required=False)

    # domain=[('is_peserta', '=', True) and ('jenis_kursus', '=', 'pemrograman')])
    # domain=[('is_peserta', '=', True) and ('kategori_pilihan', '=', 'Teknologi')]
    # domaian=[('is_peserta', '=', True)] and [('kategori_pilihan', '=', 'Teknologi')]

