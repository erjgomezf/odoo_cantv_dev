{
    'name': 'CANTV Theme Customizations',
    'version': '16.0.1.0.0',
    'category': 'Theme/Custom',
    'summary': 'Customizations for CANTV branding in Odoo 16 Community.',
    'description': """
        This module applies custom styling for CANTV branding.
        - Changes primary color to CANTV blue.
        - Updates company logo.
    """,
    'author': 'Ernesto Gomez',
    'website': 'https://www.tu-web.com',
    'depends': ['web', 'base'], # Depende del módulo web para las assets
    'data': [
        'views/custom_web_templates.xml',
        # Puedes añadir aquí un archivo de datos si quieres precargar el logo
    ],
    'assets': {
        'web.assets_backend': [ # Aplica a la interfaz de backend
            'cantv_theme/static/src/scss/custom_variables.scss',
            'cantv_theme/static/src/scss/custom_styles.scss',
        ],
        # Si quieres personalizar el frontend del sitio web, usa 'web.assets_frontend'
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}