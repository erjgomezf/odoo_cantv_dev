{
    'name': "CANTV - Extensión de Inventario",
    'summary': "Campos y funcionalidades adicionales para la gestión de inventario de fibra óptica en CANTV.",
    'version': '1.0',
    'category': 'Inventory/Inventory',
    'author': "Ernesto Gomez", # Nombre del desarrollador
    'website': "http://www.cantv.com.ve",
    'license': 'LGPL-3',
    'depends': ['stock', 'product'], # Esto es crucial
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}