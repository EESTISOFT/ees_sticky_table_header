{
    'name': 'EESTISOFT - fixed table headers',
    'version': '12.0.1.0',
    'author': 'EESTISOFT, ' 'Hideki Yamamoto',
    'category': 'Productivity',
    'website': 'https://www.eestisoft.com',
    'sequence': 2,
    'summary': 'Fixed table headers in tree views, pure css.',
	  'images':['static/description/ees_sticky_table_header.png'],
    'description': """
This module adds only 2 lines of css in the backend assets and achieves fixed table headers for listviews in search results.
============
Steps:
1-Install module
2-Restart odoo service - this is necessary to immediately rebuild the assets cache.
3-Clear browser cache and goto any odoo page with treeview and enough records to cause scrolling.
4-Scroll down and enjoy fixed table headers
    """,
    'depends': ['web'],
    'data': [
		'views/ees_sticky_table_header.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
