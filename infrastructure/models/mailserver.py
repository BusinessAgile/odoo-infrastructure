# -*- coding: utf-8 -*-
from openerp import models, fields


class mailserver(models.Model):
    """"""

    _name = 'infrastructure.mailserver'
    _inherit = 'ir.mail_server'

    partner_id = fields.Many2one(
        'res.partner',
        'Partner',
        help='If partner is set, then this mailserver will be only availble\
        for this partner databases'
        )
    external_id = fields.Char(
        'External ID',
        required=True,
        default='infra_stmp_server',
        help='External ID used to identify record on record update. It is\
        suggested that all mail servers has the same external id to make the\
        replaceable')
