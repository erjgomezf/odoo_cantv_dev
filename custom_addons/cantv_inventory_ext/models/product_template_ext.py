from odoo import fields, models

class ProductTemplateExtension(models.Model):
    _inherit = 'product.template' # Estamos extendiendo el modelo 'product.template' (plantilla de producto)

    # Campos para el inventario de fibra óptica y activos de red
    cantv_serial_number = fields.Char(string='Número de Serie Interno', copy=False, help="Identificador único interno para el activo físico.")
    cantv_acquisition_date = fields.Date(string='Fecha de Adquisición', help="Fecha en que el activo fue adquirido por CANTV.")
    cantv_estimated_lifespan = fields.Integer(string='Vida Útil Estimada (años)', help="Vida útil estimada del activo en años.")
    cantv_asset_state = fields.Selection([
        ('operational', 'Operativo'),
        ('in_maintenance', 'En Mantenimiento'),
        ('damaged', 'Dañado'),
        ('decommissioned', 'Desincorporado'),
    ], string='Estado del Activo', default='operational', help="Estado actual del activo en la red.")
    cantv_responsible_person = fields.Many2one('res.users', string='Responsable Actual', help="Usuario responsable de la custodia de este activo.")
    cantv_notes = fields.Text(string='Notas Internas', help="Cualquier observación o detalle relevante del activo.")

    # Campo para diferenciar productos de activos físicos (si es necesario)
    is_cantv_asset = fields.Boolean(string='Es Activo CANTV', default=False, help="Marcar si este producto representa un activo físico rastreable por CANTV.")

class StockMoveExtension(models.Model):
    _inherit = 'stock.move' # Extendemos el modelo de movimiento de stock

    cantv_responsible_transfer = fields.Many2one('res.users', string='Responsable de Traslado', help="Usuario que realizó este movimiento de stock.")
    cantv_transfer_notes = fields.Text(string='Notas de Traslado')

class StockPickingExtension(models.Model):
    _inherit = 'stock.picking' # Extendemos el modelo de albarán (documento de movimiento)

    cantv_responsible_picking = fields.Many2one('res.users', string='Responsable de Albarán', help="Usuario que gestionó el documento de traslado.")