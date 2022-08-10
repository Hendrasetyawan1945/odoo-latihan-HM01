from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'lainlain.lainkelas'
    _description = 'Description'

    name = fields.Char(string='Dafrar kelas Lain-lain')

    tingkatan = fields.Many2one(
        comodel_name='keterangankursus.keterangan',
        string='Keterangan Kelas lain',
        required=False)

    pengajar = fields.Many2one(
        comodel_name='pengajarku.pengajar',
        string='Pengajar',
        required=False)
    kapasitas = fields.Integer(
        string='Kapasitas Kelas',
        required=False)
    sisa = fields.Char( compute='_compute_sisa',
        string='Sisa Kelas',
        required=False)


    @api.depends('sisa')
    def _compute_sisa(self):
        for a in self:
            a.sisa = a.kapasitas














