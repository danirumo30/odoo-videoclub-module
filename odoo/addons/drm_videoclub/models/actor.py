# -*- coding: utf-8 -*-

from odoo import models, fields

class Actor(models.Model):
    _name = 'drm_videoclub.actor'
    _inherit = 'drm_videoclub.persona'
    _description = 'Actor'
    _rec_name = 'drm_nombre'

    # Relación Many2many
    drm_pelicula_ids = fields.Many2many(
        'drm_videoclub.pelicula', 
        string='Películas realizadas',
        help='Selecciona las películas en las que ha actuado'
    )