{
    'name': "CANTV - Extensión de Inventario",
    'summary': "Campos y funcionalidades adicionales para la gestión de inventario de fibra óptica en CANTV.",
    'version': '1.0',
    'category': 'Inventory/Inventory',
    'author': "Tu Nombre",
    'website': "http://www.cantv.com.ve",
    'license': 'LGPL-3',
    'depends': ['stock', 'product'], # Este módulo dependerá del módulo de inventario y producto de Odoo
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml', # Archivo donde definiremos los nuevos campos en la vista
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}