# -*- coding: utf-8 -*-

from odoo import models, fields

class Actor(models.Model):
    _name = 'drm_videoclub.actor'
    _description = 'Actor'
    
    drm_nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del actor')
    drm_nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad del actor')
    drm_fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento del actor')
    drm_biografia = fields.Text(string='Biografía', help='Introduce la biografía del actor')
    drm_foto = fields.Binary(string='Foto', help='Sube la imagen del actor')

    # Relación Many2many
    drm_pelicula_ids = fields.Many2many('drm_videoclub.pelicula', 'drm_pelicula_actor_rel', 'drm_actor_id', 'drm_pelicula_id', string='Películas en las que ha actuado')