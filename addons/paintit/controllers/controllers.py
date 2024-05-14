# -*- coding: utf-8 -*-
# from odoo import http


# class Paintit(http.Controller):
#     @http.route('/paintit/paintit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/paintit/paintit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('paintit.listing', {
#             'root': '/paintit/paintit',
#             'objects': http.request.env['paintit.paintit'].search([]),
#         })

#     @http.route('/paintit/paintit/objects/<model("paintit.paintit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('paintit.object', {
#             'object': obj
#         })

