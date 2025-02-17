# -*- coding: utf-8 -*-

from odoo import models, fields

class Pelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'Película'
    
    nombre = fields.Char(string='Título', required=True, help='Introduce el título de la película')
    sinopsis = fields.Char(string='Sinopsis', required=True, help='Introduce la sinopsis de la película')
    duracion = fields.Integer(string='Duración', help='Introduce la duración de la película en minutos')
    precio = fields.Float(string='Precio', help='Introduce el precio de la película')
    ejemplares = fields.Integer(string='Ejemplares', help='Introduce el número de ejemplares en inventario')
    fecha_salida = fields.Date(string='Fecha de salida', help='Introduce fecha de salida')
    portada = fields.Binary(string='Portada', help='Sube la imagen de la portada de la película')
    
    # Relaciones Many2Many
    categoria_ids = fields.Many2many('videoclub.categoria', string='Categorías', help='Selecciona las categorías de la película')
    actor_ids = fields.Many2many('videoclub.actor', string='Actores', help='Selecciona los actores de la película')
    
    # Relación Many2One
    director_id = fields.Many2one('videoclub.director', string='Director', help='Selecciona el director de la película')