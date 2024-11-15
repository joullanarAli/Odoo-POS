# -*- coding: utf-8 -*-
{
    'name': "tech_order1",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # relations between apps
    'depends': ['base','stock'], #unknown object has no attribue id (many to one)   settings->technical->models->product.product->In apps

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        'views/meal.xml',
        'views/order.xml',
        'views/order_tag.xml',
        'views/meal_ingredient.xml',
        'views/customer_feedback.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

