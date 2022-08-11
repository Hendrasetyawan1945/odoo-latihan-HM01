from odoo import fields, models, api


class jawa(models.Model):
    _name = 'kursusku.jawa'
    _description = 'Description Jawa'

    name = fields.Char(string='Kelas Bahasa Jawa')
    harga = fields.Integer(compute='_compute_harga',
                           string='Harga Kursus',
                           required=False)
    level_kesulitan = fields.Many2one(
        comodel_name='kursusku.tingkat',
        string='Level kesulitan Kelas',
        required=False)
    kapasitas = fields.Integer(
        string='Kapasitas Kelas',
        required=False)
    sisa = fields.Integer(compute='_compute_sisa',
                          string='Kelas yang kosong',
                          required=False)

    @api.depends('level_kesulitan')
    def _compute_harga(self):
        for a in self:
            a.harga = a.level_kesulitan.harga

    @api.depends('sisa')
    def _compute_sisa(self):
        for a in self:
            a.sisa = a.kapasitas
