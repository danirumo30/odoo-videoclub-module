# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name: 'libreria.categoria'
    _description = 'Categoria'
    
    name = fields.Char(string = 'Nombre', required = True, help = 'Introduce el nombre de la categoria')
    description = fields.Text(string = 'Descripción', help = 'Introduce la descripción')