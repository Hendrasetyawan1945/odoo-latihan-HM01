from odoo import fields, models, api


class pengajar(models.Model):
    _name = 'kursusku.pengajar'
    _description = 'Description Pengajar'

    name = fields.Char(string='Nama Pengajar')
    lusan = fields.Char(
        string='Lusan Pengajar',
        required=False)
    ttl = fields.Date(
        string='Tanggal Lahir',
        required=False)
    status = fields.Selection(
        string='Status',
        selection=[('menikah', 'Menikah'),
                   ('belum menikah', 'Belum Menikah'), ],
        required=False, )

    datapengajar_ids = fields.One2many(
        comodel_name='kursusku.python',
        inverse_name='pengajar',
        string='Datapengajar_ids',
        required=False)

