# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Actor(models.Model):
    _name = 'drm_videoclub.actor'
    _inherit = 'drm_videoclub.artista'
    _description = 'Actor'
    _rec_name = 'drm_nombre'

    # Relación Many2many
    drm_pelicula_ids = fields.Many2many(
        'drm_videoclub.pelicula', 
        string='Películas realizadas',
        help='Selecciona las películas en las que ha actuado'
    )
    
    # Campo calculado
    drm_nombre_peliculas = fields.Char(
        string='Películas', 
        compute='_compute_nombre_peliculas', 
        store=True, 
        help='Nombres de las películas separados por comas'
    )

    @api.depends('drm_pelicula_ids')
    def _compute_nombre_peliculas(self):
        for record in self:
            peliculas = record.drm_pelicula_ids.mapped('drm_nombre')
            record.drm_nombre_peliculas = ', '.join(peliculas)    