# -*- coding: utf-8 -*-

from odoo import models, fields

class Actor(models.Model):
    _name = 'videoclub.actor'
    _description = 'Actor'
    
    nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del actor')
    nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad del actor')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento del actor')
    biografia = fields.Text(string='Biografía', help='Introduce la biografía del actor')
    foto = fields.Binary(string='Foto', help='Sube la imagen del actor')

    # Relación Many2many
    pelicula_ids = fields.Many2many('videoclub.pelicula', 'pelicula_actor_rel', 'actor_id', 'pelicula_id', string='Películas en las que ha actuado')