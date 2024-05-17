# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    remote_id = fields.Integer(string="Remote ID")
    owner = fields.Char(string="Owner ID")


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    remote_id = fields.Integer(string="Remote ID")

# from odoo import models, fields, api


# class paintit(models.Model):
#     _name = 'paintit.paintit'
#     _description = 'paintit.paintit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

