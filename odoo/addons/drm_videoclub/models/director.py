# -*- coding: utf-8 -*-

from odoo import models, fields

class Director(models.Model):
    _name = 'drm_videoclub.director'
    _description = 'Director'
    
    drm_nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del director')
    drm_nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad del director')
    drm_fecha_nacimiento = fields.Datetime(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento del director')
    drm_biografia = fields.Text(string='Biografía', help='Introduce la biografía del director')
    drm_foto = fields.Binary(string='Foto', help='Sube la imagen del director')

    # Relación One2many
    drm_pelicula_ids = fields.One2many('drm_videoclub.pelicula', 'drm_director_id', string='Películas dirigidas')