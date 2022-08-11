from odoo import fields, models, api


class inggris(models.Model):
    _name = 'kursusku.inggris'
    _description = 'Description Inggris'

    name = fields.Char(string='Kelas Bahasa Inggris')
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
            
            
class bahasalain(models.Model):
    _inherit = 'kursusku.inggris'
    _name = 'kursusku.bahasalain'
    _description = "diskirpsi mencoba class"

    name = fields.Char(string='Kelas Bahasa Lain')
    negara = fields.Char(
        string='Negara', 
        required=False)
            
            
            
