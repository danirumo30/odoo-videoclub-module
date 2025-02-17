# -*- coding: utf-8 -*-

from odoo import models, fields

class Director(models.Model):
    _name = 'videoclub.director'
    _description = 'Director'
    
    nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del director')
    nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad del director')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento del director')
    biografia = fields.Text(string='Biografía', help='Introduce la biografía del director')
    foto = fields.Binary(string='Foto', help='Sube la imagen del director')

    # Relación One2many
    pelicula_ids = fields.One2many('videoclub.pelicula', 'director_id', string='Películas dirigidas')