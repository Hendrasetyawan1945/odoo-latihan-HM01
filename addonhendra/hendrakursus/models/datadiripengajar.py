from odoo import fields, models, api


class datadiripengajar(models.Model):
    _name = 'ddpengajar.datadirip'
    _description = 'Description'

    name = fields.Char(string='Kode pengajar')
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
        comodel_name='pengajarku.pengajar',
        inverse_name='datad',
        string='Datapengajar_ids',
        required=False)

