# -*- coding: utf-8 -*-

from odoo import models, fields

class Persona(models.Model):
    _name = 'drm_videoclub.persona'
    _description = 'Persona'
    
    drm_nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre')
    drm_nacionalidad = fields.Char(string='Nacionalidad', required=True, help='Introduce la nacionalidad')
    drm_fecha_nacimiento = fields.Datetime(string='Fecha de Nacimiento', help='Introduce la fecha de nacimiento')
    drm_biografia = fields.Text(string='Biografía', help='Introduce la biografía')
    drm_foto = fields.Image(string='Foto', max_width=64, max_height=64, help='Sube la imagen')
