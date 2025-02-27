# -*- coding: utf-8 -*-

from odoo import models, fields, api

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