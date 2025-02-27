# -*- coding: utf-8 -*-

from odoo import models, fields

class Director(models.Model):
    _name = 'drm_videoclub.director'
    _inherit = 'drm_videoclub.artista'
    _description = 'Director'
    _rec_name = 'drm_nombre'

    # Relación One2many
    drm_pelicula_ids = fields.One2many(
        'drm_videoclub.pelicula', 
        'drm_director_id', 
        string='Películas dirigidas',
        help='Selecciona las películas que ha dirigido'
    )