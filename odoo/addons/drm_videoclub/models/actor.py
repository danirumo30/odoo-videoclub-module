# -*- coding: utf-8 -*-

from odoo import models, fields

class Actor(models.Model):
    _name = 'drm_videoclub.actor'
    _inherit = 'drm_videoclub.persona'
    _description = 'Actor'
    _rec_name = 'drm_nombre'
    
    drm_nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del actor')
    drm_nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad del actor')
    drm_fecha_nacimiento = fields.Datetime(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento del actor')
    drm_biografia = fields.Text(string='Biografía', help='Introduce la biografía del actor')
    drm_foto = fields.Image(string='Foto', max_width = 64, max_height = 64, help='Sube la imagen del actor')

    # Relación Many2many
    drm_pelicula_ids = fields.Many2many(
        'drm_videoclub.pelicula', 
        string='Películas realizadas',
        help='Selecciona las películas en las que ha actuado'
    )