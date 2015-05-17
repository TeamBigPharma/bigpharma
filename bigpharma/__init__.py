"""
bigpharma - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'bigpharma.schema'
    flow_module   = 'bigpharma.flow'
    javascripts   = [
        'js/bigpharma/routes.js',
        'js/opal/controllers/discharge.js',
        'js/bigpharma/controllers/formulation.js'
    ]
