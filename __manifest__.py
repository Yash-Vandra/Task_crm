{
    'name':"Task",
    'depends':['crm','purchase','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/crm_stage_views.xml',
        'views/vendor_type_views.xml',
        'views/respartner_views.xml',
        'views/purchaseorder_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}