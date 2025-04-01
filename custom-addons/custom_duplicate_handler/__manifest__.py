{
    'name': 'Custom Duplicate Handler',
    'version': '1.0',
    'summary': 'Handles duplicates in CRM and res.partner models',
    'author': 'Melnychenko Yehor',
    'category': 'CRM',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}