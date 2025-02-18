# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name = 'drm_videoclub.categoria'
    _description = 'Categoria'
    
    drm_nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre de la categoría')
