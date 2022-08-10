from odoo import fields, models, api


class tingkat(models.Model):
    _name = 'kursusku.tingkat'
    _description = 'tingkat '

    name = fields.Selection(string='Tingkatan Pembelajaran',
                            selection=[('low','Low'),('easy','Easy'),('normal','Normal'),('hard','Hard')])
    keterangan = fields.Char(
        string='Keterangan Pemberlajaran',
        required=False)

    harga = fields.Integer(
        string='Harga Kursus',
        required=False)

    tingkat_ids = fields.One2many(
        comodel_name='kursusku.python',
        inverse_name='level_kesulitan',
        string='Id tingkatan',
        required=False)





