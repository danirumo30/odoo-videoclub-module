# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name = 'videoclub.categoria'
    _description = 'Categoria'
    
    nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre de la categoría')
    
    # Relación Many2many
    pelicula_ids = fields.Many2many('videoclub.pelicula', 'pelicula_categoria_rel', 'categoria_id', 'pelicula_id', string='Películas de esta categoría')
