from odoo import fields, models, api


class python(models.Model):
    _name = 'kursusku.python'
    _description = 'Kategori '

    name = fields.Char(string='Kelas python')

    harga = fields.Integer(compute='_compute_harga',
        string='Harga Kursus',
        required=False)
    pengajar = fields.Many2one(
        comodel_name='kursusku.pengajar',
        string='Pengajar',
        required=False)

    level_kesulitan = fields.Many2one(
        comodel_name='kursusku.tingkat',
        string='Level kesulitan Kelas',
        required=False)
    kapasitas = fields.Integer(
        string='Kapasitas Kelas',
        required=False)
    jum_siswa_prog = fields.Integer(
        string='Jumplah Siswa',
        required=False)
    sisa = fields.Integer(
        compute='_compute_sisa',
        string='Kelas yang kosong',
        required=False)


    @api.depends('jum_siswa_prog')
    def _compute_sisa(self):
        for i in self:
            i.sisa = i.kapasitas - i.jum_siswa_prog

    @api.depends('level_kesulitan')
    def _compute_harga(self):
        for a in self:
            a.harga=a.level_kesulitan.harga





    # @api.depends('sisa')
    # def _compute_sisa(self):
    #     for a in self:
    #         a.sisa = a.kapasitas


# class java(models.Model):
#     _inherit = 'kursusku.python'
#     _name = 'kursusku.java'
#     _description = 'kelas Java'
#     starup = fields.Char(
#         string='Starup',
#         required=False)



