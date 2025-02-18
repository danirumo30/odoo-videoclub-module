# -*- coding: utf-8 -*-

from odoo import models, fields

class Pelicula(models.Model):
    _name = 'drm_videoclub.pelicula'
    _description = 'Película'
    
    drm_nombre = fields.Char(string='Título', required=True, help='Introduce el título de la película')
    drm_sinopsis = fields.Char(string='Sinopsis', required=True, help='Introduce la sinopsis de la película')
    drm_duracion = fields.Integer(string='Duración', help='Introduce la duración de la película en minutos')
    drm_precio = fields.Float(string='Precio', help='Introduce el precio de la película')
    drm_ejemplares = fields.Integer(string='Ejemplares', help='Introduce el número de ejemplares en inventario')
    drm_fecha_salida = fields.Datetime(string='Fecha de salida', default = fields.Datetime.now, help='Introduce fecha de salida')
    drm_portada = fields.Image(string='Portada', max_width = 64, max_height = 64, help='Sube la imagen de la portada de la película')
    
    # Relaciones Many2Many
    drm_categoria_ids = fields.Many2many('drm_videoclub.categoria', string='Categorías', help='Selecciona las categorías de la película')
    drm_actor_ids = fields.Many2many('drm_videoclub.actor', string='Actores', help='Selecciona los actores de la película')
    
    # Relación Many2One
    drm_director_id = fields.Many2one('drm_videoclub.director', string='Director', help='Selecciona el director de la película')