# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pelicula(models.Model):
    _name = 'drm_videoclub.pelicula'
    _description = 'Película'
    _rec_name = 'drm_nombre'
    
    drm_nombre = fields.Char(string='Título', required=True, help='Introduce el título de la película')
    drm_sinopsis = fields.Char(string='Sinopsis', required=True, help='Introduce la sinopsis de la película')
    drm_duracion = fields.Integer(string='Duración', help='Introduce la duración de la película en minutos')
    drm_precio = fields.Float(string='Precio', help='Introduce el precio de la película')
    drm_ejemplares = fields.Integer(string='Ejemplares', help='Introduce el número de ejemplares en inventario')
    drm_fecha_salida = fields.Datetime(string='Fecha de salida', default = fields.Datetime.now, help='Introduce fecha de salida')
    drm_portada = fields.Image(string='Portada', max_width = 64, max_height = 64, help='Sube la imagen de la portada de la película')
    drm_fecha_inicio = fields.Date("Fecha inicio")
    drm_fecha_fin = fields.Date("Fecha fin")
    
    # Relaciones Many2Many
    drm_categoria_ids = fields.Many2many(
        'drm_videoclub.categoria', 
        string='Categorías', 
        help='Selecciona las categorías de la película'
    )
    drm_actor_ids = fields.Many2many(
        'drm_videoclub.actor', 
        string='Actores', 
        help='Selecciona los actores de la película'
    )
    
    # Relación Many2One
    drm_director_id = fields.Many2one(
        'drm_videoclub.director', 
        string='Director', 
        help='Selecciona el director de la película'
    )
    
    # Campos calculados
    drm_nombre_actores = fields.Char(
        string='Actores', 
        compute='_compute_nombre_actores', 
        store=True, 
        help='Nombres de los actores separados por comas'
    )

    @api.depends('drm_actor_ids')
    def _compute_nombre_actores(self):
        for record in self:
            actores = record.drm_actor_ids.mapped('drm_nombre')
            record.drm_nombre_actores = ', '.join(actores)
      
    drm_nombre_categorias = fields.Char(
        string='Categorias', 
        compute='_compute_nombre_categorias', 
        store=True, 
        help='Nombres de las categorias separados por comas'
    )

    @api.depends('drm_categoria_ids')
    def _compute_nombre_categorias(self):
        for record in self:
            categorias = record.drm_categoria_ids.mapped('drm_nombre')
            record.drm_nombre_categorias = ', '.join(categorias)      
    
    # Restricciones Python
    @api.constrains('drm_precio')
    def _check_precio(self):
        for record in self:
            if record.drm_precio <= 0:
                raise ValidationError("El precio de la película debe ser mayor que 0 €.")

    @api.constrains('drm_duracion')
    def _check_duracion(self):
        for record in self:
            if record.drm_duracion <= 0:
                raise ValidationError("La duración de la película debe ser mayor que 0 minutos.")
          
    # Restricciones SQL  
    _sql_constraints = [
        ('check_precio', 'CHECK(drm_precio >= 0)', 'El precio de la película no puede ser negativo.'),
        ('check_duracion', 'CHECK(drm_duracion >= 0)', 'La duración de la película no puede ser negativa.')
    ]